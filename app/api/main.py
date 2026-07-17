from fastapi import FastAPI
from app.api.router import api_router


api_app = FastAPI()


api_app.include_router(api_router)
