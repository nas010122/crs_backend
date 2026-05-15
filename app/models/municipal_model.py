from sqlalchemy import Column, Integer, String, Text, ForeignKey
from app.database.db import Base

class MunicipalRecord(Base):
    __tablename__ = "municipal_records"
    id = Column(Integer, primary_key=True, index=True)
    request_id = Column(Integer, ForeignKey("service_requests.id"))
    assigned_department = Column(String)
    action_taken = Column(Text)