from pathlib import Path

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy import func
from sqlalchemy.orm import Session

from app.core.security import admin_user
from app.db.database import get_db
from app.db.models import ChatMessage, DiseasePrediction, User

router = APIRouter()
KB_DIR = Path(__file__).resolve().parents[2] / "knowledge_base"


class KnowledgeDocumentIn(BaseModel):
    content: str = Field(min_length=1, max_length=200_000)


def _user_summary(user: User) -> dict:
    return {"id": user.id, "name": user.name, "email": user.email, "phone": user.phone,
            "created_at": user.created_at.isoformat() if user.created_at else None}


@router.get("/stats")
def stats(_: User = Depends(admin_user), db: Session = Depends(get_db)):
    return {
        "users": db.query(func.count(User.id)).scalar() or 0,
        "chat_messages": db.query(func.count(ChatMessage.id)).scalar() or 0,
        "disease_predictions": db.query(func.count(DiseasePrediction.id)).scalar() or 0,
        "knowledge_documents": len(list(KB_DIR.glob("*.txt"))) + len(list(KB_DIR.glob("*.md"))),
    }


@router.get("/users")
def users(_: User = Depends(admin_user), db: Session = Depends(get_db)):
    return [_user_summary(user) for user in db.query(User).order_by(User.created_at.desc()).limit(500).all()]


@router.get("/chats")
def chats(_: User = Depends(admin_user), db: Session = Depends(get_db)):
    rows = db.query(ChatMessage).order_by(ChatMessage.created_at.desc()).limit(200).all()
    return [{"id": row.id, "user_id": row.user_id, "message": row.message, "response": row.response,
             "language": row.language, "created_at": row.created_at.isoformat()} for row in rows]


@router.get("/disease-records")
def disease_records(_: User = Depends(admin_user), db: Session = Depends(get_db)):
    rows = db.query(DiseasePrediction).order_by(DiseasePrediction.created_at.desc()).limit(200).all()
    return [{"id": row.id, "user_id": row.user_id, "crop": row.crop, "disease": row.disease,
             "confidence": row.confidence, "image_path": row.image_path,
             "created_at": row.created_at.isoformat()} for row in rows]


@router.get("/knowledge")
def knowledge(_: User = Depends(admin_user)):
    KB_DIR.mkdir(exist_ok=True)
    return [{"name": path.name, "content": path.read_text(encoding="utf-8")} for path in sorted(KB_DIR.glob("*.txt"))]


@router.put("/knowledge/{filename}")
def update_knowledge(filename: str, data: KnowledgeDocumentIn, _: User = Depends(admin_user)):
    safe_name = Path(filename).name
    if safe_name != filename or Path(safe_name).suffix.lower() not in {".txt", ".md"}:
        raise HTTPException(status_code=400, detail="Only .txt and .md knowledge files are allowed")
    KB_DIR.mkdir(exist_ok=True)
    (KB_DIR / safe_name).write_text(data.content, encoding="utf-8")
    return {"message": "Knowledge document updated", "name": safe_name}
