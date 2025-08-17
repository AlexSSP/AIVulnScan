# Infrastructure Vulnerability Scanner with AI

AI-powered infrastructure vulnerability detection system for cloud and on-premise environments.

## 🌟 Features
- **AI-Driven Analysis**: Uses machine learning models to detect complex vulnerabilities
- **Multi-Format Support**: Works with Terraform, Kubernetes, Docker Compose, and cloud formation templates
- **Prioritized Results**: Classifies vulnerabilities by severity (critical, high, medium, low)
- **REST API**: Easy integration with CI/CD pipelines and security tools
- **Infrastructure as Code**: Full containerization with Docker support

## 🛠️ Technologies
- **Backend**: Python 3.10, FastAPI
- **AI Engine**: TensorFlow/PyTorch (model-dependent)
- **Containerization**: Docker
- **Data Validation**: Pydantic

## 📦 Installation & Running

### Prerequisites
- Python 3.10+
- Docker
- GPU (recommended for AI processing)

## 🔧 Model Management

### Using Custom Models
1. Place your model files in `app/models/`
2. Set environment variable:
```bash

export AI_MODEL_PATH=/app/models/your_model.h5

# Clone repository
git clone https://github.com/saleny/AIVulnScan.git
cd AIVulnScan

# Install dependencies
pip install -r requirements.txt

# Start service
uvicorn app.main:app --reload