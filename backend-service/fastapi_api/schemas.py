from pydantic import BaseModel
from datetime import datetime


#using pydentic creating basemodel
class ConversionLogBase(BaseModel):
    filename: str
    timestamp: datetime
    status: str

    class Config:
        orm_mode = True
