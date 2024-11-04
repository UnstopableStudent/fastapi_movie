from src.movies.router import router as movies_router
from fastapi import FastAPI, Depends
from fastapi_users import FastAPIUsers

from src.registration.base_config import User
from src.registration.manager import get_user_manager
from src.registration.registration import auth_backend
from src.registration.schemas import UserRead, UserCreate

app = FastAPI(
    title="Movie App"
)
fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

app.include_router(movies_router)

app.include_router(fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],)

app.include_router(fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],)


@app.get("/main")
async def main():
    return {"data": "Movie"}

current_user = fastapi_users.current_user()


@app.get("/protected-route")
def protected_route(user: User = Depends(current_user)):
    return f"Hello, {user.username}"


@app.get("/unprotected-route")
def unprotected_route():
    return f"Hello, anonym"

