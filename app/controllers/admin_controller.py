from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.db import get_db
from app.models.admin_model import AuditLog
from app.schemas.admin_schema import AuditLogBase

router = APIRouter(prefix="/admin", tags=["8. System Admin"])

@router.post("/logs")
def create_audit(data: AuditLogBase, db: Session = Depends(get_db)):
    new_log = AuditLog(**data.dict())
    db.add(new_log)
    db.commit()
    return new_log

@router.get("/logs")
def get_audits(db: Session = Depends(get_db)):
    return db.query(AuditLog).all()

@router.delete("/logs/{id}")
def delete_audit(id: int, db: Session = Depends(get_db)):
    log = db.query(AuditLog).filter(AuditLog.id == id).first()
    db.delete(log)
    db.commit()
    return {"message": "Audit log deleted"}