from app.config import settings
from .model_loader import load_model


class VulnerabilityModel:
    def __init__(self):
        self.model = load_model()

    def predict(self, input_data):
        return self.model.predict(input_data)