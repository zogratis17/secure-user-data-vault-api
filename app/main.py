from fastapi import FastAPI

app = FastAPI(
    title="Secure User Data Vault API",
    description="A secure REST API for encrypted user data storage",
    version="0.1.0"
)


@app.get("/health", tags=["Health"])
def health_check():
    """
    Health check endpoint to verify service status.
    """
    return {"status": "ok"}
