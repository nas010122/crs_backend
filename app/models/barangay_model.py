from sqlalchemy import Column, Integer, Text, ForeignKey, Boolean
from app.database.db import Base

class BarangayRecord(Base):
    __tablename__ = "barangay_records"
    id = Column(Integer, primary_key=True, index=True)
    request_id = Column(Integer, ForeignKey("service_requests.id"))
    officer_remarks = Column(Text)
    is_verified = Column(Boolean, default=False)