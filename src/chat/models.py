#DB and Alembic message structures
from sqlalchemy import Table, Column, Integer, String, MetaData
from pydantic import BaseModel

metadata = MetaData()

messages = Table(
    "messages",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("message", String)
)

class MessagesModel(BaseModel):
    id: int
    message: int


