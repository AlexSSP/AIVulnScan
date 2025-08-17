from fastapi import FastAPI
from app.routes import scan

app = FastAPI(
    title="Infra Vulnerability Scanner API",
    description="AI-powered infrastructure vulnerability detection",
    version="0.1.0"
)

app.include_router(scan.router, prefix="/api/v1")

@app.get("/health")
def health_check():
    return {"status": "healthy"}