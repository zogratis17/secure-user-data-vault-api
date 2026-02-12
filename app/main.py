from fastapi import FastAPI
from app.config import settings
from app.routes import auth
from app.routes import vault
from fastapi.middleware.cors import CORSMiddleware

from app.utils.dependencies import get_current_user
from fastapi import Depends

app = FastAPI(
    title=settings.APP_NAME,
    description="A secure REST API for encrypted user data storage",
    version="0.1.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(vault.router)


@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "ok"}


@app.get("/protected")
def protected(user_id: str = Depends(get_current_user)):
    return {"message": f"Hello user {user_id}"}

from fastapi.responses import JSONResponse
from fastapi.requests import Request


@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal server error"}
    )
