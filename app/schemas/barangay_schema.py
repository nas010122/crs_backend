from pydantic import BaseModel
from typing import Optional

class BarangayBase(BaseModel):
    request_id: int
    officer_remarks: str
    is_verified: bool

class BarangayUpdate(BaseModel):
    officer_remarks: Optional[str] = None
    is_verified: Optional[bool] = None

class BarangayResponse(BarangayBase):
    id: int
    class Config:
        from_attributes = True