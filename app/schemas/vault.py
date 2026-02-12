from pydantic import BaseModel, Field, field_validator


class VaultCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    data: str = Field(..., min_length=1)

    @field_validator("title")
    def clean_title(cls, v):
        return v.strip()


class VaultResponse(BaseModel):
    id: str
    title: str
    data: str
