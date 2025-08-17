from fastapi import APIRouter, HTTPException
from app.ai.vulnerabilities import analyze_infrastructure
from app.schemas.scan import ScanRequest, ScanResponse

router = APIRouter()

@router.post("/scan", response_model=ScanResponse)
async def scan_infrastructure(request: ScanRequest):
    try:
        results = analyze_infrastructure(request.config)
        return {"vulnerabilities": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))