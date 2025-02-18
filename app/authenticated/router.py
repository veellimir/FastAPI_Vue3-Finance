from fastapi import APIRouter, Depends
from fastapi_users import FastAPIUsers

from .manager import get_user_manager
from .auth import auth_backend

from app.users.models import User
from app.users.schemas import UserRead, UserCreate, UserUpdate

fastapi_users = FastAPIUsers(
    get_user_manager,
    [auth_backend],
    User,
    UserRead,
    UserCreate,
    UserUpdate,
)

router = APIRouter()

router.include_router(fastapi_users.get_auth_router(auth_backend), prefix="/auth/jwt", tags=["auth"])
router.include_router(fastapi_users.get_register_router(), prefix="/auth", tags=["auth"])
router.include_router(fastapi_users.get_users_router(), prefix="/users", tags=["users"])
