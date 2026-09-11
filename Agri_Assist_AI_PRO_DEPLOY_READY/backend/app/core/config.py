from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "Agri Assist AI"
    secret_key: str = "change-me"
    admin_email: str = ""
    database_url: str = "sqlite:///./agri_assist.db"
    gemini_api_key: str = ""
    gemini_model: str = "gemini-2.5-flash"
    openweather_api_key: str = ""
    vector_store: str = "local"
    chroma_persist_dir: str = "vector_store"
    cors_origins: str = "*"
    upload_dir: str = "uploads"
    model_config = SettingsConfigDict(env_file=Path(__file__).resolve().parents[2] / ".env", extra="ignore")

settings = Settings()
