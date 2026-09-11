from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.db.database import Base, engine
from app.api import auth, profile, chat, weather, disease, fertilizer, crops, preferences, admin

Base.metadata.create_all(bind=engine)
app = FastAPI(title=settings.app_name, version="1.0.0")

origins = ["*"] if settings.cors_origins == "*" else [x.strip() for x in settings.cors_origins.split(",")]
app.add_middleware(CORSMiddleware, allow_origins=origins, allow_credentials=True,
                   allow_methods=["*"], allow_headers=["*"])

app.include_router(auth.router, prefix="/api/auth", tags=["Auth"])
app.include_router(profile.router, prefix="/api/profile", tags=["Profile"])
app.include_router(chat.router, prefix="/api/chat", tags=["AI Chat"])
app.include_router(weather.router, prefix="/api/weather", tags=["Weather"])
app.include_router(disease.router, prefix="/api/disease", tags=["Disease"])
app.include_router(fertilizer.router, prefix="/api/fertilizer", tags=["Fertilizer"])
app.include_router(crops.router, prefix="/api/crops", tags=["Crops"])
app.include_router(preferences.router, prefix="/api/preferences", tags=["Preferences"])
app.include_router(admin.router, prefix="/api/admin", tags=["Admin"])

@app.get("/")
def root():
    return {"app": settings.app_name, "status": "running"}

@app.get("/health")
def health():
    return {"status": "ok"}
