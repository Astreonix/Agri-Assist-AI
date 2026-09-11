from pathlib import Path
import numpy as np
from PIL import Image
from app.core.config import settings

MODEL = Path(__file__).resolve().parents[2] / "ml_model" / "crop_disease.keras"
CLASSES = Path(__file__).resolve().parents[2] / "ml_model" / "classes.txt"

def disease_guidance(label: str) -> dict:
    normalized = label.lower().replace("_", " ")
    if "healthy" in normalized:
        return {
            "information": "The model found visual patterns consistent with a healthy leaf.",
            "management_guidance": "Continue regular scouting, balanced irrigation, sanitation and monitoring for new symptoms.",
        }
    return {
        "information": f"The model found visual patterns associated with {label}. Similar symptoms can have multiple causes, so confirm in the field.",
        "management_guidance": "Isolate or mark affected plants, inspect both sides of leaves, improve sanitation, avoid prolonged leaf wetness, and seek local extension advice before treatment.",
    }


def local_predict(image_path: str):
    if not MODEL.exists() or not CLASSES.exists():
        return {"ready": False, "message": "Local disease model is not trained."}

    try:
        import tensorflow as tf
    except ImportError:
        return {"ready": False, "message": "TensorFlow is not installed. Install backend/requirements-ml.txt to use the local model."}
    model = tf.keras.models.load_model(MODEL)
    labels = [x.strip() for x in CLASSES.read_text(encoding="utf-8").splitlines() if x.strip()]
    if not labels:
        return {"ready": False, "message": "The local disease model has no class labels."}
    image = Image.open(image_path).convert("RGB").resize((224, 224))
    arr = np.asarray(image, dtype=np.float32) / 255.0
    pred = model.predict(np.expand_dims(arr, 0), verbose=0)[0]
    idx = int(np.argmax(pred))
    return {
        "ready": True,
        "source": "local_model",
        "disease": labels[idx],
        "confidence": float(pred[idx]),
        "top3": [
            {"label": labels[int(i)], "confidence": float(pred[int(i)])}
            for i in np.argsort(pred)[-3:][::-1]
        ],
        **disease_guidance(labels[idx]),
    }

def gemini_vision_predict(image_path: str, mime_type: str = "image/jpeg"):
    if not settings.gemini_api_key:
        return {"ready": False, "message": "GEMINI_API_KEY is not configured."}

    from google import genai
    from google.genai import types

    client = genai.Client(api_key=settings.gemini_api_key)
    data = Path(image_path).read_bytes()
    prompt = """You are an agriculture image-analysis assistant.
Inspect this crop/leaf image. Return ONLY valid JSON with:
possible_disease, confidence_percent, visible_symptoms, immediate_management,
prevention, disclaimer.
If the image is unclear, say "Uncertain" and explain why.
Do not claim a diagnosis is confirmed. Do not provide dangerous or unsupported pesticide
mixing instructions or invented doses. Recommend local agricultural extension advice
and product-label instructions for exact treatment."""
    response = client.models.generate_content(
        model=settings.gemini_model,
        contents=[
            types.Part.from_bytes(data=data, mime_type=mime_type),
            prompt,
        ],
        config=types.GenerateContentConfig(temperature=0.2, response_mime_type="application/json"),
    )
    import json
    try:
        result = json.loads(response.text)
    except Exception:
        result = {"raw_analysis": response.text}
    return {
        "ready": True,
        "source": "gemini_vision",
        "disease": result.get("possible_disease", "Uncertain"),
        "confidence": float(result.get("confidence_percent", 0)) / 100,
        **result,
    }

def predict(image_path: str, mime_type: str = "image/jpeg"):
    local = local_predict(image_path)
    if local.get("ready"):
        return local
    return gemini_vision_predict(image_path, mime_type)
