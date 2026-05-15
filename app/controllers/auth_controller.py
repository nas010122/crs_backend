from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.database.db import get_db
from app.models.auth_model import User
from app.schemas.auth_schema import UserCreate, UserUpdate
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
router = APIRouter() # Inalis ang prefix dito dahil nasa main.py na ito

# --- HELPERS ---
def get_password_hash(password):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

# --- LOGIN (Dito magtatama ang Lock Icon) ---
@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    # Hardcoded check para sa testing mo ngayon
    if form_data.username == "admin" and form_data.password == "admin123":
        return {"access_token": "token-aljan-andy", "token_type": "bearer"}
    
    # DB Check
    user = db.query(User).filter(User.username == form_data.username).first()
    if not user or not verify_password(form_data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password"
        )
    return {"access_token": f"access-{user.username}", "token_type": "bearer"}

# --- CRUD ROUTES ---
@router.post("/register")
def register_user(data: UserCreate, db: Session = Depends(get_db)):
    new_user = User(
        username=data.username,
        email=data.email,
        full_name=data.full_name,
        password=get_password_hash(data.password),
        role=data.role
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "Success", "user": new_user.username}

@router.get("/users")
def get_all_users(db: Session = Depends(get_db)):
    return db.query(User).all()