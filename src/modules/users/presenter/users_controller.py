from fastapi import APIRouter

users_router = APIRouter(prefix="/users")


@users_router.get("/")
async def get_users():
    pass


@users_router.post("/{user_id}")
async def create_user():
    pass