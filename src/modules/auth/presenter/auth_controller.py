from fastapi import APIRouter
from src.common.dependencies.auth.fastapi_users import fastapi_users
from src.common.dependencies.auth.auth_backend import authentication_backend
from src.modules.auth.presenter.schemas.user_schema import UserRead, UserCreate

auth_router = APIRouter(prefix="/api/v1/auth", tags=["auth"])

auth_router.include_router(
    router=fastapi_users.get_auth_router(authentication_backend)
)

auth_router.include_router(
    router=fastapi_users.get_register_router(UserRead, UserCreate),
)

auth_router.include_router(
    router=fastapi_users.get_verify_router(UserRead),
)

auth_router.include_router(
    router=fastapi_users.get_reset_password_router(),
)