from datetime import datetime
from pydantic import BaseModel


# Operation Schema
class OperationCreate(BaseModel):
    id: int
    quantity: str
    figi: str
    instrument_type: str
    date: datetime
    type: str
