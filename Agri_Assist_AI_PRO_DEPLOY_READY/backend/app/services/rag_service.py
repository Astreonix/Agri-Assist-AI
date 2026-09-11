from pathlib import Path
import hashlib
import re
from collections import Counter
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from app.core.config import settings

KB_DIR = Path(__file__).resolve().parents[2] / "knowledge_base"
TOKEN_PATTERN = re.compile(r"[\w'-]+", re.UNICODE)
CHUNK_SIZE = 1200
CHUNK_OVERLAP = 180
INDEX_PATH = KB_DIR / ".rag_vector_index.joblib"

def _tokens(text: str) -> list[str]:
    return [token.lower() for token in TOKEN_PATTERN.findall(text)]


def _chunks(name: str, text: str) -> list[dict]:
    words = text.split()
    chunks = []
    start = 0
    while start < len(words):
        end = min(start + CHUNK_SIZE, len(words))
        chunks.append({"source": name, "text": " ".join(words[start:end])})
        if end == len(words):
            break
        start = max(end - CHUNK_OVERLAP, start + 1)
    return chunks


def _documents() -> list[dict]:
    documents = []
    for path in sorted(KB_DIR.glob("*.txt")) + sorted(KB_DIR.glob("*.md")):
        documents.extend(_chunks(path.name, path.read_text(encoding="utf-8")))
    return documents


def _signature(documents: list[dict]) -> str:
    content = "\n".join(f"{item['source']}:{item['text']}" for item in documents)
    return hashlib.sha256(content.encode("utf-8")).hexdigest()


def _vector_index(documents: list[dict]) -> tuple[TfidfVectorizer, object]:
    signature = _signature(documents)
    if INDEX_PATH.exists():
        try:
            index = joblib.load(INDEX_PATH)
            if index["signature"] == signature:
                return index["vectorizer"], index["matrix"]
        except (EOFError, OSError, ValueError):
            pass
    vectorizer = TfidfVectorizer(token_pattern=r"(?u)\b[\w'-]+\b", ngram_range=(1, 2), min_df=1)
    matrix = vectorizer.fit_transform([item["text"] for item in documents])
    joblib.dump({"signature": signature, "vectorizer": vectorizer, "matrix": matrix}, INDEX_PATH)
    return vectorizer, matrix


def _retrieve_chroma(query: str, documents: list[dict], top_k: int) -> list[dict] | None:
    if settings.vector_store.lower() != "chroma":
        return None
    try:
        import chromadb
        client = chromadb.PersistentClient(path=settings.chroma_persist_dir)
        collection = client.get_or_create_collection("agri_knowledge")
        collection.upsert(
            ids=[f"{item['source']}:{index}" for index, item in enumerate(documents)],
            documents=[item["text"] for item in documents],
            metadatas=[{"source": item["source"]} for item in documents],
        )
        result = collection.query(query_texts=[query], n_results=min(top_k, len(documents)))
        return [
            {"source": metadata["source"], "text": text, "score": round(1 - float(distance), 4)}
            for text, metadata, distance in zip(
                result["documents"][0], result["metadatas"][0], result["distances"][0]
            )
        ]
    except (ImportError, RuntimeError, ValueError):
        return None


def retrieve_with_sources(query: str, top_k: int = 3) -> list[dict]:
    KB_DIR.mkdir(exist_ok=True)
    chunks = _documents()
    if not chunks:
        return []

    chroma_matches = _retrieve_chroma(query, chunks, top_k)
    if chroma_matches is not None:
        return chroma_matches

    vectorizer, matrix = _vector_index(chunks)
    query_vector = vectorizer.transform([query])
    scores = cosine_similarity(query_vector, matrix).ravel()
    scored = sorted(((float(score), chunk) for score, chunk in zip(scores, chunks) if score > 0),
                    key=lambda item: item[0], reverse=True)
    selected = []
    sources = set()
    for score, chunk in scored:
        if chunk["source"] in sources and len(selected) < top_k - 1:
            continue
        selected.append({**chunk, "score": round(score, 4)})
        sources.add(chunk["source"])
        if len(selected) == top_k:
            break
    return selected


def retrieve(query: str, top_k: int = 3) -> str:
    matches = retrieve_with_sources(query, top_k)
    return "\n\n".join(f"[{match['source']}]\n{match['text']}" for match in matches)
