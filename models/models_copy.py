from sqlalchemy import MetaData,  Table, Integer, String, TIMESTAMP, ForeignKey, Column, JSON, Boolean
from datetime import datetime

from sqlalchemy.orm import mapped_column

metadate = MetaData()

role = Table(
    "role",
    metadate,
    mapped_column("id", Integer, primary_key=True),
    mapped_column("name", String, nullable=False),
    mapped_column("permissions", JSON),
)

user = Table(
    "user",
    metadate,
    mapped_column("id", Integer, primary_key=True),
    mapped_column("email", String, nullable=False),
    mapped_column("username", String, nullable=False),
    mapped_column("hashed_password", String, nullable=False),
    mapped_column("registered_at", TIMESTAMP, default=datetime.utcnow),
    mapped_column("role_id", Integer, ForeignKey(role.c.id)),
    mapped_column("is_active", Boolean, default=True, nullable=False),
    mapped_column("is_superuser", Boolean, default=False, nullable=False),
    mapped_column("is_verified", Boolean, default=False, nullable=False),
)
