from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas.vault import VaultCreate, VaultResponse
from app.models.vault import VaultModel
from app.database import mongodb
from app.utils.dependencies import get_current_user
from app.core.encryption import encryption_service

router = APIRouter(prefix="/vault", tags=["Vault"])


@router.post("/", response_model=VaultResponse, status_code=status.HTTP_201_CREATED)
def create_vault_entry(
    item: VaultCreate,
    user_id: str = Depends(get_current_user)
):
    """
    Store encrypted user data.
    """

    encrypted = encryption_service.encrypt(item.data)

    vault = VaultModel(
        user_id=user_id,
        title=item.title,
        encrypted_data=encrypted
    )

    result = mongodb.vault.insert_one(vault.to_dict())

    return {
        "id": str(result.inserted_id),
        "title": item.title,
        "data": item.data
    }


@router.get("/", response_model=list[VaultResponse])
def get_user_vault(user_id: str = Depends(get_current_user)):
    """
    Retrieve all vault entries for authenticated user.
    """

    items = mongodb.vault.find({"user_id": str(user_id)})


    results = []
    for item in items:
        try:
            decrypted = encryption_service.decrypt(item["encrypted_data"])
        except Exception:
            decrypted = "[Decryption failed]"


        results.append({
            "id": str(item["_id"]),
            "title": item["title"],
            "data": decrypted
        })

    return results
