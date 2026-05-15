from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.db import get_db
from app.models.barangay_model import BarangayRecord
from app.schemas.barangay_schema import BarangayBase, BarangayUpdate

router = APIRouter(prefix="/barangay", tags=["3. Barangay Management"])

@router.post("/")
def create_brgy_record(data: BarangayBase, db: Session = Depends(get_db)):
    new_rec = BarangayRecord(**data.dict())
    db.add(new_rec)
    db.commit()
    return new_rec

@router.get("/")
def list_brgy_records(db: Session = Depends(get_db)):
    return db.query(BarangayRecord).all()

@router.patch("/{id}")
def update_brgy(id: int, data: BarangayUpdate, db: Session = Depends(get_db)):
    rec = db.query(BarangayRecord).filter(BarangayRecord.id == id).first()
    for k, v in data.dict(exclude_unset=True).items(): setattr(rec, k, v)
    db.commit()
    return {"message": "Brgy record updated"}

@router.delete("/{id}")
def delete_brgy(id: int, db: Session = Depends(get_db)):
    rec = db.query(BarangayRecord).filter(BarangayRecord.id == id).first()
    db.delete(rec)
    db.commit()
    return {"message": "Deleted"}