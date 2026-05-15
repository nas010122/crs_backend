from pydantic import BaseModel
from typing import Optional

class RequestBase(BaseModel):
    title: str
    description: str
    request_type: str

class RequestCreate(RequestBase):
    citizen_id: int

class RequestUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None

class RequestResponse(RequestBase):
    id: int
    status: str
    current_level: str
    class Config:
        from_attributes = True