from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.db import get_db
from app.models.auth_model import User
from app.schemas.auth_schema import UserCreate, UserUpdate

router = APIRouter(prefix="/auth", tags=["1. User Management"])

@router.post("/")
def register_user(data: UserCreate, db: Session = Depends(get_db)):
    new_user = User(**data.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get("/")
def get_all_users(db: Session = Depends(get_db)):
    return db.query(User).all()

@router.put("/{user_id}")
def update_user(user_id: int, data: UserUpdate, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user: raise HTTPException(status_code=404, detail="User not found")
    for k, v in data.dict(exclude_unset=True).items(): setattr(user, k, v)
    db.commit()
    return {"message": "User updated"}

@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    db.delete(user)
    db.commit()
    return {"message": "User deleted"}