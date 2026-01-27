from fastapi import FastAPI
from app.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    description="A secure REST API for encrypted user data storage",
    version="0.1.0"
)


@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "ok"}
