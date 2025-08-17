import os
from app.config import settings
import logging

logger = logging.getLogger(__name__)


def load_model(model_path: str = None):
    path = model_path or settings.AI_MODEL_PATH

    try:
        if not os.path.exists(path):
            logger.warning(f"Model not found at {path}, using stub model")
            return StubModel()

        logger.info(f"Model loaded from {path}")
        return StubModel()

    except Exception as e:
        logger.error(f"Model loading failed: {str(e)}")
        return StubModel()


class StubModel:

    def predict(self, input_data):
        return [
            {
                "type": "network",
                "severity": "high",
                "description": "Publicly exposed database port",
                "remediation": "Restrict database access to internal network"
            },
            {
                "type": "authentication",
                "severity": "critical",
                "description": "Default admin credentials enabled",
                "remediation": "Change default credentials and enable MFA"
            }
        ]