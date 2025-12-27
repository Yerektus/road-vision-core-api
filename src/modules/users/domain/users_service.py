import modules.users.data.users_repository as users_repository
from sqlalchemy.ext.asyncio import AsyncSession
from modules.users.dto.user_dto import UserDto
from common.mapper.users.users_mapper import map_user_model_to_dto

def get_users(session: AsyncSession) -> list[UserDto]:
    users_model = users_repository.get_users(session=session) 

    return list(map(map_user_model_to_dto, users_model))

def get_user_by_id(session: AsyncSession, user_id: int) -> UserDto:
    user_model = users_repository.get_user_by_id(session=session, user_id=user_id)

    return map_user_model_to_dto(user_model)