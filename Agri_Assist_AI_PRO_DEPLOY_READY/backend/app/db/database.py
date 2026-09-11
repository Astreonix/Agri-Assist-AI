from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from app.core.config import settings

database_url = settings.database_url
if database_url.startswith("sqlite:///") and database_url != "sqlite:///:memory:":
    sqlite_path = Path(database_url.removeprefix("sqlite:///"))
    if not sqlite_path.is_absolute():
        sqlite_path = Path(__file__).resolve().parents[2] / sqlite_path
    database_url = f"sqlite:///{sqlite_path.as_posix()}"

connect_args = {"check_same_thread": False} if database_url.startswith("sqlite") else {}
engine = create_engine(database_url, connect_args=connect_args)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
