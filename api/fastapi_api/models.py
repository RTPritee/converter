from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from database import Base

#to keep track/log
class ConversionLog(Base):
    __tablename__ = "conversion_logs"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)
    status = Column(String, nullable=False)
