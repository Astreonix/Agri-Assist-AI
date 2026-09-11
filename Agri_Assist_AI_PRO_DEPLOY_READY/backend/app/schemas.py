from pydantic import BaseModel, EmailStr, Field

class RegisterIn(BaseModel):
    name: str = Field(min_length=2, max_length=120)
    email: EmailStr
    password: str = Field(min_length=6)
    phone: str = ""

class LoginIn(BaseModel):
    email: EmailStr
    password: str

class ProfileIn(BaseModel):
    farm_size: float = 0
    location: str = ""
    soil_type: str = ""
    main_crop: str = ""
    irrigation_type: str = ""

class ChatIn(BaseModel):
    message: str
    language: str = "auto"

class FertilizerIn(BaseModel):
    crop: str
    growth_stage: str
    soil_type: str = ""
    farm_size: float = 0

class CropAdviceIn(BaseModel):
    crop: str
    topic: str
    growth_stage: str = ""
    soil_type: str = ""

class PreferenceIn(BaseModel):
    language: str = "English"
    temperature_unit: str = "metric"
    notifications_enabled: bool = True
