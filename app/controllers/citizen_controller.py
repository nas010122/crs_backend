from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.db import get_db
from app.models.citizen_model import ServiceRequest
from app.schemas.citizen_schema import RequestCreate, RequestUpdate

router = APIRouter(prefix="/citizen", tags=["2. Citizen Requests"])

@router.post("/")
def submit_request(data: RequestCreate, db: Session = Depends(get_db)):
    new_req = ServiceRequest(**data.dict(), current_level="BARANGAY", status="Pending")
    db.add(new_req)
    db.commit()
    db.refresh(new_req)
    return new_req

@router.get("/{citizen_id}")
def view_requests(citizen_id: int, db: Session = Depends(get_db)):
    return db.query(ServiceRequest).filter(ServiceRequest.citizen_id == citizen_id).all()

@router.patch("/{id}")
def update_request(id: int, data: RequestUpdate, db: Session = Depends(get_db)):
    req = db.query(ServiceRequest).filter(ServiceRequest.id == id).first()
    for k, v in data.dict(exclude_unset=True).items(): setattr(req, k, v)
    db.commit()
    return {"message": "Request updated"}

@router.delete("/{id}")
def delete_request(id: int, db: Session = Depends(get_db)):
    req = db.query(ServiceRequest).filter(ServiceRequest.id == id).first()
    db.delete(req)
    db.commit()
    return {"message": "Deleted"}