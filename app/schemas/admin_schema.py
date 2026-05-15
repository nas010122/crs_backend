from pydantic import BaseModel
from datetime import datetime

class AuditLogBase(BaseModel):
    action: str
    admin_id: int
    details: str

class AuditLogResponse(AuditLogBase):
    id: int
    timestamp: datetime
    class Config:
        from_attributes = True