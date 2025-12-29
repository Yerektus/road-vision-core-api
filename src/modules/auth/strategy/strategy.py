from fastapi import Depends
from fastapi_users_db_sqlalchemy.access_token import AccessTokenDatabase
from src.common.models.access_token import AccessToken
from fastapi_users.authentication.strategy.db import DatabaseStrategy
from src.common.models.access_token import AccessToken
from src.config.config import settings

def get_database_strategy(access_token_db: AccessTokenDatabase[AccessToken] = Depends(get_access_token_db)) -> DatabaseStrategy:
    return DatabaseStrategy(
        access_token_db,
        settings.access_toeken_settings.access_token_expire
    )