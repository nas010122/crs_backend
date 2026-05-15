from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.db import get_db
from app.models.provincial_model import ProvincialRecord
from app.schemas.provincial_schema import ProvincialBase, ProvincialUpdate

router = APIRouter(prefix="/provincial", tags=["5. Provincial Management"])

@router.post("/")
def create_prov(data: ProvincialBase, db: Session = Depends(get_db)):
    new_rec = ProvincialRecord(**data.dict())
    db.add(new_rec)
    db.commit()
    return new_rec

@router.get("/")
def list_prov(db: Session = Depends(get_db)):
    return db.query(ProvincialRecord).all()

@router.patch("/{id}")
def update_prov(id: int, data: ProvincialUpdate, db: Session = Depends(get_db)):
    rec = db.query(ProvincialRecord).filter(ProvincialRecord.id == id).first()
    for k, v in data.dict(exclude_unset=True).items(): setattr(rec, k, v)
    db.commit()
    return {"message": "Updated"}

@router.delete("/{id}")
def delete_prov(id: int, db: Session = Depends(get_db)):
    rec = db.query(ProvincialRecord).filter(ProvincialRecord.id == id).first()
    db.delete(rec)
    db.commit()
    return {"message": "Deleted"}