from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(120), nullable=False)
    email = Column(String(255), unique=True, index=True, nullable=False)
    phone = Column(String(40), default="")
    password_hash = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    profile = relationship("FarmerProfile", back_populates="user", uselist=False, cascade="all, delete")

class FarmerProfile(Base):
    __tablename__ = "farmer_profiles"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True)
    farm_size = Column(Float, default=0)
    location = Column(String(255), default="")
    soil_type = Column(String(100), default="")
    main_crop = Column(String(100), default="")
    irrigation_type = Column(String(100), default="")
    user = relationship("User", back_populates="profile")

class ChatMessage(Base):
    __tablename__ = "chat_messages"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    message = Column(Text, nullable=False)
    response = Column(Text, nullable=False)
    language = Column(String(40), default="auto")
    created_at = Column(DateTime, default=datetime.utcnow)

class DiseasePrediction(Base):
    __tablename__ = "disease_predictions"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    crop = Column(String(100), default="")
    disease = Column(String(150), default="")
    confidence = Column(Float, default=0)
    image_path = Column(String(500), default="")
    created_at = Column(DateTime, default=datetime.utcnow)

class WeatherSearch(Base):
    __tablename__ = "weather_searches"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    location = Column(String(255), default="")
    temperature_c = Column(Float, nullable=True)
    humidity = Column(Float, nullable=True)
    wind_mps = Column(Float, nullable=True)
    description = Column(String(255), default="")
    configured = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)

class UserPreference(Base):
    __tablename__ = "user_preferences"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True, nullable=False)
    language = Column(String(40), default="English")
    temperature_unit = Column(String(10), default="metric")
    notifications_enabled = Column(Integer, default=1)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
