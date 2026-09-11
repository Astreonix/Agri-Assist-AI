from pathlib import Path
from uuid import uuid4
from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from sqlalchemy.orm import Session
from app.core.config import settings
from app.core.security import current_user
from app.db.database import get_db
from app.db.models import DiseasePrediction
from app.services.disease_service import predict

router=APIRouter()
MAX_IMAGE_BYTES = 10 * 1024 * 1024

@router.post("/analyze")
async def analyze(file:UploadFile=File(...),user=Depends(current_user),db:Session=Depends(get_db)):
    if not file.content_type or not file.content_type.startswith("image/"):
        raise HTTPException(400,"Please upload an image")
    content = await file.read(MAX_IMAGE_BYTES + 1)
    if len(content) > MAX_IMAGE_BYTES:
        raise HTTPException(413, "Image must be 10 MB or smaller")
    d=Path(settings.upload_dir); d.mkdir(exist_ok=True)
    filename = Path(file.filename or "leaf.jpg").name
    path=d/f"{uuid4().hex}_{filename}"
    path.write_bytes(content)
    result=predict(str(path), file.content_type)
    if not result.get("ready"): return result
    db.add(DiseasePrediction(user_id=user.id,disease=result["disease"],confidence=result["confidence"],image_path=str(path)))
    db.commit()
    return result
