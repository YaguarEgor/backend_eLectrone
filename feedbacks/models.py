from sqlalchemy import ForeignKey, MetaData, Table, Column, TIMESTAMP, UUID, String, Integer

metadata = MetaData()

feedbacks = Table(
    "feedback",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String, nullable=False),
    Column("all_text", String, nullable=True),
    Column("author", String, nullable=False)
)