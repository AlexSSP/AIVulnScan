from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from app.routes import scan, auth, admin
from app.logging_config import setup_logging
from app.dependencies import get_current_active_user
from app.config import settings
from prometheus_fastapi_instrumentator import Instrumentator

setup_logging()

app = FastAPI(
    title="Infra Vulnerability Scanner API",
    description="AI-powered infrastructure vulnerability detection",
    version="1.0.0",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
    openapi_url="/api/openapi.json"
)

#DEV
if settings.DEBUG:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(auth.router, prefix="/api/v1")
app.include_router(scan.router, prefix="/api/v1")
app.include_router(
    admin.router,
    prefix="/api/v1/admin",
    dependencies=[Depends(get_current_active_user)]
)

Instrumentator().instrument(app).expose(app)

@app.get("/api/health")
def health_check():
    return {
        "status": "healthy",
        "environment": settings.ENV,
        "debug": settings.DEBUG,
        "version": app.version
    }

@app.get("/")
def root():
    return {
        "message": "AI Vulnerability Scanner API",
        "docs": "/api/docs",
        "redoc": "/api/redoc"
    }