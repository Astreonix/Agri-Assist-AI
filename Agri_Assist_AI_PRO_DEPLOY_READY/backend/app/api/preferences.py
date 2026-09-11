from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.security import current_user
from app.db.database import get_db
from app.db.models import UserPreference
from app.schemas import PreferenceIn

router = APIRouter()


def _get_or_create(user_id: int, db: Session) -> UserPreference:
    preference = db.query(UserPreference).filter(UserPreference.user_id == user_id).first()
    if not preference:
        preference = UserPreference(user_id=user_id)
        db.add(preference)
        db.flush()
    return preference


@router.get("")
def get_preferences(user=Depends(current_user), db: Session = Depends(get_db)):
    preference = _get_or_create(user.id, db)
    db.commit()
    return {
        "language": preference.language,
        "temperature_unit": preference.temperature_unit,
        "notifications_enabled": bool(preference.notifications_enabled),
    }


@router.put("")
def update_preferences(data: PreferenceIn, user=Depends(current_user), db: Session = Depends(get_db)):
    preference = _get_or_create(user.id, db)
    preference.language = data.language
    preference.temperature_unit = data.temperature_unit
    preference.notifications_enabled = int(data.notifications_enabled)
    db.commit()
    return {"message": "Preferences updated"}