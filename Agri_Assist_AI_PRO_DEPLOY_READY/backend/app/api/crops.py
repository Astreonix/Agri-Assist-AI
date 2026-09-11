from fastapi import APIRouter, Depends
from app.core.security import current_user
from app.schemas import CropAdviceIn
from app.services.rag_service import retrieve
from app.services.ai_service import answer_with_gemini

router=APIRouter()

@router.get("")
def crops(user=Depends(current_user)):
    return {"crops": ["Wheat", "Rice", "Cotton", "Maize", "Tomato", "Potato", "Chili"]}

@router.post("/advice")
def advice(data:CropAdviceIn,user=Depends(current_user)):
    q=f"Crop: {data.crop}; Topic: {data.topic}; Growth stage: {data.growth_stage}; Soil: {data.soil_type}"
    return {"advice":answer_with_gemini(q,retrieve(q))}
