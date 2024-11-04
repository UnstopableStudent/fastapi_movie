from typing import Any

from fastapi import APIRouter, Depends, requests
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from src.movies import schemas
from src.movies.models import Movie
from src.movies.schemas import ReadMovie

router = APIRouter(
    prefix="/movies",
    tags=["Movies"]
)


@router.get("/", response_model=list[ReadMovie])
async def read_movie(movie_title: str, session: AsyncSession = Depends(get_async_session)) -> Any:
    query = select(Movie).where(Movie.title == movie_title)
    result = await session.execute(query)
    return result.scalars().all()

@router.post("/")
async def create_movie(movies: schemas.CreateMovie, session: AsyncSession = Depends(get_async_session)):
    new_movie = insert(Movie).values(**movies.model_dump())
    await session.execute(new_movie)
    await session.commit()
    return {"status": "Movie added"}