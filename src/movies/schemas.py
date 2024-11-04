from typing import Optional

from pydantic import BaseModel


class CreateMovie(BaseModel):
    title: str
    year: int
    director: str

class ReadMovie(BaseModel):
    title: str
    year: int
    director: str
