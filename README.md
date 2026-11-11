> **GCP retirement — 11 November 2026:** Cloud deployment is archived and shut down. Historical cloud URLs and deployment examples below are retained as reference. Do not run them. See [retirement records](docs/gcp-retirement/README.md).

# Ubuntu Troubleshooting Helper

Minimal FastAPI service that provides troubleshooting steps for common Ubuntu issues.

## Run locally
pip install -r requirements.txt
uvicorn app:app --reload

## Run with Docker
docker build -t ubuntu-troubleshooter .
docker run -p 8080:8080 ubuntu-troubleshooter

## Endpoints
- GET /health
- POST /diagnose
