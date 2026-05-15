from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from app.database.db import Base

class ProvincialRecord(Base):
    __tablename__ = "provincial_records"
    id = Column(Integer, primary_key=True, index=True)
    request_id = Column(Integer, ForeignKey("service_requests.id"))
    approval_code = Column(String, unique=True)
    is_funded = Column(Boolean, default=False)