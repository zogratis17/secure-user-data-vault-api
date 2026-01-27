from pydantic import BaseSettings


class Settings(BaseSettings):
    # Application
    APP_NAME: str = "Secure User Data Vault API"

    # Security
    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # Encryption
    FERNET_KEY: str

    # Database
    MONGO_URI: str

    class Config:
        env_file = ".env"


settings = Settings()
