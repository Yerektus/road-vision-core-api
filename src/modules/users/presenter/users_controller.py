from fastapi import APIRouter, Depends
from src.common.dependencies.auth.fastapi_users import fastapi_users
from sqlalchemy.ext.asyncio import AsyncSession
from src.common.database.db_helper import db_helper
import src.modules.users.domain.users_service as users_service
from src.modules.auth.presenter.schemas.user_schema import UserRead, UserUpdate

users_router = APIRouter(prefix="/api/v1/users", tags=["users"])

users_router.include_router(
    router=fastapi_users.get_users_router(UserRead, UserUpdate),
)


@users_router.get("")
async def get_users(
    session: AsyncSession = Depends(db_helper.scoped_session_depedency),
):
    return await users_service.get_users(session=session)
