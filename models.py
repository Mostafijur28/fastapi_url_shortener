from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from database import Base

class URL(Base):
    __tablename__ = "urls"

    id = Column(Integer, primary_key=True, index=True)
    original_url = Column(String, nullable=False)
    shortened_url = Column(String, unique=True, nullable=False)
    creation_time = Column(DateTime, default=datetime.utcnow)
    expiration_time = Column(DateTime, nullable=False)

class AccessLog(Base):
    __tablename__ = "access_logs"

    id = Column(Integer, primary_key=True, index=True)
    shortened_url = Column(String, nullable=False)
    access_time = Column(DateTime, default=datetime.utcnow)
    ip_address = Column(String)
