from pydantic import BaseModel


class ScanRequest(BaseModel):
    config: str 


class VulnerabilityItem(BaseModel):
    type: str
    severity: str
    description: str


class ScanResponse(BaseModel):
    vulnerabilities: list[VulnerabilityItem]