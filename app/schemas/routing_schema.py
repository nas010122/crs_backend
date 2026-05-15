from pydantic import BaseModel
from datetime import datetime

class RoutingBase(BaseModel):
    request_id: int
    from_level: str
    to_level: str
    reason: str

class RoutingResponse(RoutingBase):
    id: int
    escalated_at: datetime
    class Config:
        from_attributes = True