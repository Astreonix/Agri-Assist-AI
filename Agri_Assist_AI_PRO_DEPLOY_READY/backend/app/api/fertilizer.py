from fastapi import APIRouter, Depends
from app.core.security import current_user
from app.schemas import FertilizerIn
from app.services.ai_service import answer_with_gemini

router=APIRouter()

@router.post("/recommend")
def recommend(data:FertilizerIn,user=Depends(current_user)):
    q=f"""Give cautious nutrient-management guidance for crop={data.crop}, stage={data.growth_stage},
soil={data.soil_type}, farm_size={data.farm_size}. Do not invent exact fertilizer doses.
Explain that soil testing and local extension guidance should determine exact rates."""
    return {"recommendation":answer_with_gemini(q)}
