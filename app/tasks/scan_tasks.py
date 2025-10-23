from celery import Celery
from app.config import settings
from app.ai.vulnerabilities import analyze_infrastructure
import time

celery_app = Celery(
    "scan_tasks",
    broker=settings.CELERY_BROKER_URL,
    backend=settings.CELERY_RESULT_BACKEND
)


@celery_app.task
def async_scan_task(file_path: str):
    time.sleep(5)

    try:
        results = analyze_infrastructure(file_path)
        return {"status": "success", "results": results}
    except Exception as e:
        return {"status": "error", "message": str(e)}