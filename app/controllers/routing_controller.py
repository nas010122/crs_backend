from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.db import get_db
from app.models.routing_model import EscalationLog
from app.schemas.routing_schema import RoutingBase

router = APIRouter(prefix="/routing", tags=["6. Smart Routing"])

@router.post("/")
def create_log(data: RoutingBase, db: Session = Depends(get_db)):
    new_log = EscalationLog(**data.dict())
    db.add(new_log)
    db.commit()
    return new_log

@router.get("/{request_id}")
def get_logs(request_id: int, db: Session = Depends(get_db)):
    return db.query(EscalationLog).filter(EscalationLog.request_id == request_id).all()

@router.delete("/{id}")
def delete_log(id: int, db: Session = Depends(get_db)):
    log = db.query(EscalationLog).filter(EscalationLog.id == id).first()
    db.delete(log)
    db.commit()
    return {"message": "Log deleted"}