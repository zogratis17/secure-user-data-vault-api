from fastapi import FastAPI
from app.config import settings]
from app.routes import auth


app = FastAPI(
    title=settings.APP_NAME,
    description="A secure REST API for encrypted user data storage",
    version="0.1.0"
)
app.include_router(auth.router)


@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "ok"}
