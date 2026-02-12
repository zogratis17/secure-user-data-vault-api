from datetime import datetime
from typing import Optional


class VaultModel:
    """
    Database model for stored vault data.
    """

    def __init__(
        self,
        user_id: str,
        title: str,
        encrypted_data: str,
        created_at: Optional[datetime] = None
    ):
        self.user_id = user_id
        self.title = title
        self.encrypted_data = encrypted_data
        self.created_at = created_at or datetime.utcnow()

    def to_dict(self) -> dict:
        return {
            "user_id": self.user_id,
            "title": self.title,
            "encrypted_data": self.encrypted_data,
            "created_at": self.created_at,
        }
