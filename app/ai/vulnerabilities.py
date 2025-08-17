from app.ai.model import VulnerabilityModel
import json
import logging

logger = logging.getLogger(__name__)
model = VulnerabilityModel()

def analyze_infrastructure(config: str):
    try:
        parsed_config = json.loads(config)
        logger.debug(f"Analyzing config: {parsed_config}")
        return model.predict(parsed_config)
    except json.JSONDecodeError:
        logger.error("Invalid JSON configuration")
        raise ValueError("Invalid JSON format in configuration")
    except Exception as e:
        logger.exception("Analysis error")
        raise RuntimeError(f"Analysis failed: {str(e)}")