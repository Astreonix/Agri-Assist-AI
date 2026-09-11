from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.core.security import current_user
from app.db.database import get_db
from app.db.models import WeatherSearch
from app.services.weather_service import get_weather

router=APIRouter()

@router.get("")
async def weather(lat:float=Query(..., ge=-90, le=90),lon:float=Query(..., ge=-180, le=180),user=Depends(current_user),db:Session=Depends(get_db)):
    result = await get_weather(lat, lon)
    db.add(WeatherSearch(user_id=user.id, latitude=lat, longitude=lon,
                         location=result.get("location", ""),
                         temperature_c=result.get("temperature_c"),
                         humidity=result.get("humidity"), wind_mps=result.get("wind_mps"),
                         description=result.get("description", ""),
                         configured=1 if result.get("configured") else 0))
    db.commit()
    return result
