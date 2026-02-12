from datetime import datetime
from typing import Optional


class UserModel:
    """
    Database model for a user.
    This represents how data is stored in MongoDB.
    """

    def __init__(
        self,
        email: str,
        hashed_password: str,
        created_at: Optional[datetime] = None
    ):
        self.email = email
        self.hashed_password = hashed_password
        self.created_at = created_at or datetime.utcnow()

    def to_dict(self) -> dict:
        """
        Convert model to MongoDB-compatible dict.
        """
        return {
            "email": self.email,
            "hashed_password": self.hashed_password,
            "created_at": self.created_at,
        }
