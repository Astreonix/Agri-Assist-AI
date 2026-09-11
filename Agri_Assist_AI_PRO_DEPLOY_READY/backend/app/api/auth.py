from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.db.models import User, FarmerProfile, UserPreference
from app.schemas import RegisterIn, LoginIn
from app.core.security import hash_password, verify_password, create_access_token

router = APIRouter()

@router.post("/register")
def register(data: RegisterIn, db: Session = Depends(get_db)):
    if db.query(User).filter(User.email == data.email).first():
        raise HTTPException(409, "Email already registered")
    user = User(name=data.name, email=data.email, phone=data.phone, password_hash=hash_password(data.password))
    db.add(user); db.flush()
    db.add(FarmerProfile(user_id=user.id))
    db.add(UserPreference(user_id=user.id))
    db.commit()
    return {"access_token": create_access_token(user.id), "token_type": "bearer"}

@router.post("/login")
def login(data: LoginIn, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == data.email).first()
    if not user or not verify_password(data.password, user.password_hash):
        raise HTTPException(401, "Incorrect email or password")
    return {"access_token": create_access_token(user.id), "token_type": "bearer"}
