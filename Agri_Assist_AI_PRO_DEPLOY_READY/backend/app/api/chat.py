from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.db.models import ChatMessage, FarmerProfile
from app.schemas import ChatIn
from app.core.security import current_user
from app.services.rag_service import retrieve_with_sources
from app.services.ai_service import answer_with_gemini

router = APIRouter()

@router.post("")
def chat(data: ChatIn, user=Depends(current_user), db: Session=Depends(get_db)):
    p = db.query(FarmerProfile).filter(FarmerProfile.user_id == user.id).first()
    profile = {"farm_size":p.farm_size if p else 0,"location":p.location if p else "",
               "soil_type":p.soil_type if p else "","main_crop":p.main_crop if p else "",
               "irrigation_type":p.irrigation_type if p else ""}
    matches = retrieve_with_sources(data.message)
    context = "\n\n".join(f"[{match['source']}]\n{match['text']}" for match in matches)
    answer = answer_with_gemini(data.message, context, profile, data.language)
    db.add(ChatMessage(user_id=user.id,message=data.message,response=answer,language=data.language))
    db.commit()
    return {"response":answer,"sources_available":bool(matches),
            "sources":[match["source"] for match in matches]}

@router.get("/history")
def history(user=Depends(current_user), db: Session=Depends(get_db)):
    rows=db.query(ChatMessage).filter(ChatMessage.user_id==user.id).order_by(ChatMessage.created_at.desc()).limit(50).all()
    return [{"id":x.id,"message":x.message,"response":x.response,"created_at":x.created_at.isoformat()} for x in rows]
