from sqlalchemy.orm import DeclarativeBase
from .db import async_session_maker


class Base(DeclarativeBase):
    pass


async def get_async_session():
    async with async_session_maker() as session:
        yield session
