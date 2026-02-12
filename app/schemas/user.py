from pydantic import BaseModel, EmailStr, Field


class UserRegister(BaseModel):
    """
    Request schema for user registration.
    """
    email: EmailStr = Field(..., example="user@example.com")
    password: str = Field(..., min_length=8, example="StrongPass123")


class UserLogin(BaseModel):
    """
    Request schema for user login.
    """
    email: EmailStr = Field(..., example="user@example.com")
    password: str = Field(..., example="StrongPass123")


class UserResponse(BaseModel):
    """
    Response schema for user-related responses.
    """
    id: str
    email: EmailStr
