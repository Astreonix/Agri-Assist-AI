from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.db.models import FarmerProfile
from app.schemas import ProfileIn
from app.core.security import current_user
from app.core.config import settings

router = APIRouter()

@router.get("")
def get_profile(user=Depends(current_user), db: Session=Depends(get_db)):
    p = db.query(FarmerProfile).filter(FarmerProfile.user_id == user.id).first()
    return {"name":user.name,"email":user.email,"phone":user.phone,
            "is_admin":bool(settings.admin_email and user.email.casefold() == settings.admin_email.casefold()),
            "farm_size":p.farm_size if p else 0,"location":p.location if p else "",
            "soil_type":p.soil_type if p else "","main_crop":p.main_crop if p else "",
            "irrigation_type":p.irrigation_type if p else ""}

@router.put("")
def update_profile(data: ProfileIn, user=Depends(current_user), db: Session=Depends(get_db)):
    p = db.query(FarmerProfile).filter(FarmerProfile.user_id == user.id).first()
    if not p:
        p = FarmerProfile(user_id=user.id); db.add(p)
    for k,v in data.model_dump().items(): setattr(p,k,v)
    db.commit()
    return {"message":"Profile updated"}
