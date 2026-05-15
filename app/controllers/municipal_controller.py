from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.db import get_db
from app.models.municipal_model import MunicipalRecord
from app.schemas.municipal_schema import MunicipalBase, MunicipalUpdate

router = APIRouter(prefix="/municipal", tags=["4. Municipal Management"])

@router.post("/")
def create_muni(data: MunicipalBase, db: Session = Depends(get_db)):
    new_rec = MunicipalRecord(**data.dict())
    db.add(new_rec)
    db.commit()
    return new_rec

@router.get("/")
def list_muni(db: Session = Depends(get_db)):
    return db.query(MunicipalRecord).all()

@router.patch("/{id}")
def update_muni(id: int, data: MunicipalUpdate, db: Session = Depends(get_db)):
    rec = db.query(MunicipalRecord).filter(MunicipalRecord.id == id).first()
    for k, v in data.dict(exclude_unset=True).items(): setattr(rec, k, v)
    db.commit()
    return {"message": "Updated"}

@router.delete("/{id}")
def delete_muni(id: int, db: Session = Depends(get_db)):
    rec = db.query(MunicipalRecord).filter(MunicipalRecord.id == id).first()
    db.delete(rec)
    db.commit()
    return {"message": "Deleted"}