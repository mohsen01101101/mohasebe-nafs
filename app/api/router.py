from fastapi import APIRouter
from app.api.auth import router as auth_router
from app.api.users import router as users_router
from app.api.lists import router as lists_router
from app.api.actions import router as actions_router


api_router = APIRouter()


api_router.include_router(auth_router)
api_router.include_router(users_router)
api_router.include_router(lists_router)
api_router.include_router(actions_router)
