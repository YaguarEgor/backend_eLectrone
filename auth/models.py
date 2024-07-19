from sqlalchemy import  MetaData, Table, Column, TIMESTAMP, UUID, String, Boolean, Integer

metadata = MetaData()

user = Table(
    "user",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("email", String, unique=True, nullable=False),
    Column("name", String, nullable=False),
    Column("second_name", String, nullable=False),
    Column("hashed_password", String, nullable=False),
    Column("is_active", Boolean, default=True, nullable=False),
    Column("is_verified", Boolean, default=False, nullable=False),
    Column("is_superuser", Boolean, default=False, nullable=False),
)