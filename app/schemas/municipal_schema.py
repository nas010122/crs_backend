from pydantic import BaseModel
from typing import Optional

class MunicipalBase(BaseModel):
    request_id: int
    assigned_department: str
    action_taken: str

class MunicipalUpdate(BaseModel):
    assigned_department: Optional[str] = None
    action_taken: Optional[str] = None

class MunicipalResponse(MunicipalBase):
    id: int
    class Config:
        from_attributes = True