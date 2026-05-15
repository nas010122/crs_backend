from pydantic import BaseModel
from typing import Optional

class ProvincialBase(BaseModel):
    request_id: int
    approval_code: str
    is_funded: bool

class ProvincialUpdate(BaseModel):
    is_funded: Optional[bool] = None

class ProvincialResponse(ProvincialBase):
    id: int
    class Config:
        from_attributes = True