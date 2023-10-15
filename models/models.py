from sqlalchemy import MetaData,  Table, Column, Integer, String, TIMESTAMP, ForeignKey, Column, JSON
from datetime import datetime

metadate = MetaData()

roles = Table(
    "roles",
    metadate,
    Column("id", Integer, primary_key=True),
    Column("name", String,nullable=False),
    Column("permissions", JSON),
)

users = Table(
    "users",
    metadate,
    Column("id", Integer, primary_key=True),
    Column("email", String, nullable=False),
    Column("username", String, nullable=False),
    Column("password", String, nullable=False),
    Column("registered_at", TIMESTAMP, default=datetime.utcnow),
    Column("role_id", Integer,ForeignKey("roles.id")),
)