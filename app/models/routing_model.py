from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from app.database.db import Base

class EscalationLog(Base):
    __tablename__ = "escalation_logs"
    id = Column(Integer, primary_key=True, index=True)
    request_id = Column(Integer, ForeignKey("service_requests.id"))
    from_level = Column(String)
    to_level = Column(String)
    reason = Column(String)
    escalated_at = Column(DateTime(timezone=True), server_default=func.now())