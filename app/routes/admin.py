from fastapi import APIRouter, Depends, HTTPException
from app.dependencies import get_current_active_user
from app.schemas.user import User
from app.tasks.scan_tasks import async_scan_task
from celery.result import AsyncResult

router = APIRouter(
    prefix="/admin",
    tags=["Administration"],
    dependencies=[Depends(get_current_active_user)]
)

@router.get("/task/{task_id}")
def get_task_status(task_id: str):
    task_result = AsyncResult(task_id)
    return {
        "task_id": task_id,
        "status": task_result.status,
        "result": task_result.result
    }

@router.post("/purge-cache")
def purge_cache():
    # Логика очистки кэша
    return {"status": "cache cleared"}