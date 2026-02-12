from pydantic import BaseModel, Field


class VaultCreate(BaseModel):
    """
    Request schema for creating a vault entry.
    """
    title: str = Field(..., example="GitHub Token")
    data: str = Field(..., example="ghp_xxxxxxxxx")


class VaultResponse(BaseModel):
    """
    Response schema for vault data.
    """
    id: str
    title: str
    data: str
