from fastapi_users.db import SQLAlchemyBaseUserTableUUID
from sqlalchemy import Column, String

from settings.database.base import Base


class User(SQLAlchemyBaseUserTableUUID, Base):
    username = Column(String, nullable=False, unique=True)
