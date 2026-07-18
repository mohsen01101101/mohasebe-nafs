from pydantic import BaseModel, Field


class AuthRegister(BaseModel):
    phone_number: str
    name: str
    password: str = Field(min_length=8)


class AuthLogin(BaseModel):
    phone_number: str
    password: str = Field(min_length=8)


class TokenResponse(BaseModel):
    access_token: str
    token_type: str
