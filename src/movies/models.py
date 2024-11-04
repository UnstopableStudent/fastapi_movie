from sqlalchemy import MetaData
from sqlalchemy.orm import mapped_column, Mapped


from database import Base

metadata = MetaData()
class Movie(Base):
    __tablename__ = "movie"
    metadata = metadata
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(nullable=False)
    year: Mapped[int] = mapped_column(nullable=False)
    director: Mapped[str] = mapped_column(nullable=False)
