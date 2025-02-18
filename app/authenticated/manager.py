from fastapi_users import BaseUserManager, UUIDIDMixin
from fastapi import Depends

from fastapi_users.db import SQLAlchemyUserDatabase

from app.users.models import User
from settings.database.base import get_async_session, async_session_maker


class UserManager(UUIDIDMixin, BaseUserManager[User, str]):
    user_db_model = User


async def get_user_db(session=Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)


async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)
