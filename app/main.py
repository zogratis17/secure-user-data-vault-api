from fastapi import FastAPI
from app.config import settings
from app.routes import auth
from app.routes import vault

from app.utils.dependencies import get_current_user
from fastapi import Depends

app = FastAPI(
    title=settings.APP_NAME,
    description="A secure REST API for encrypted user data storage",
    version="0.1.0"
)
app.include_router(auth.router)
app.include_router(vault.router)


@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "ok"}


@app.get("/protected")
def protected(user_id: str = Depends(get_current_user)):
    return {"message": f"Hello user {user_id}"}
