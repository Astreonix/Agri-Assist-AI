import httpx
from fastapi import HTTPException
from app.core.config import settings

async def get_weather(lat: float, lon: float):
    if not settings.openweather_api_key:
        return {"configured": False, "message": "OPENWEATHER_API_KEY is not configured."}
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"lat": lat, "lon": lon, "appid": settings.openweather_api_key, "units": "metric"}
    async with httpx.AsyncClient(timeout=15) as client:
        r = await client.get(url, params=params)
    if r.status_code != 200:
        raise HTTPException(502, "Weather provider error")
    d = r.json()
    return {
        "configured": True,
        "location": d.get("name", ""),
        "temperature_c": d.get("main", {}).get("temp"),
        "humidity": d.get("main", {}).get("humidity"),
        "wind_mps": d.get("wind", {}).get("speed"),
        "description": (d.get("weather") or [{}])[0].get("description", ""),
    }
