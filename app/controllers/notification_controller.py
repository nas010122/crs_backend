from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.db import get_db
from app.models.notification_model import Notification
from app.schemas.notification_schema import NotificationBase, NotificationUpdate

router = APIRouter(prefix="/notifications", tags=["7. Notifications"])

@router.post("/")
def create_notif(data: NotificationBase, db: Session = Depends(get_db)):
    new_notif = Notification(**data.dict())
    db.add(new_notif)
    db.commit()
    return new_notif

@router.get("/{user_id}")
def get_user_notifs(user_id: int, db: Session = Depends(get_db)):
    return db.query(Notification).filter(Notification.user_id == user_id).all()

@router.patch("/{id}")
def mark_read(id: int, db: Session = Depends(get_db)):
    notif = db.query(Notification).filter(Notification.id == id).first()
    notif.is_read = True
    db.commit()
    return {"message": "Read"}

@router.delete("/{id}")
def delete_notif(id: int, db: Session = Depends(get_db)):
    notif = db.query(Notification).filter(Notification.id == id).first()
    db.delete(notif)
    db.commit()
    return {"message": "Deleted"}