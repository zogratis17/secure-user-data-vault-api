from cryptography.fernet import Fernet
from app.config import settings


class EncryptionService:
    """
    Handles encryption and decryption of sensitive data
    using Fernet (AES symmetric encryption).
    """

    def __init__(self, key: str):
        self.fernet = Fernet(key.encode())

    def encrypt(self, plain_text: str) -> str:
        """
        Encrypt plaintext data.
        """
        encrypted = self.fernet.encrypt(plain_text.encode())
        return encrypted.decode()

    def decrypt(self, encrypted_text: str) -> str:
        """
        Decrypt encrypted data.
        """
        decrypted = self.fernet.decrypt(encrypted_text.encode())
        return decrypted.decode()


encryption_service = EncryptionService(settings.FERNET_KEY)
