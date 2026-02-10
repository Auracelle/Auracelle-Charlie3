# Auracelle Charlie – Web Services Architecture

This repository provides the official **Auracelle Charlie Research Engine** backend.
It exposes a FastAPI-based web service used for policy stress-testing,
computational governance analysis, and strategic decision science simulations.

## Architecture Overview
- **Backend:** FastAPI (policy evaluation, metrics, health checks)
- **Frontend:** Streamlit (Mission Console)
- **Deployment:** Docker-ready for Render, Fly.io, Railway, Azure, or AWS

## Local Development

```bash
docker-compose up --build
```

API will be available at:
```
http://localhost:8000/v1/health
```

## Example Endpoints
- `GET /v1/health`
- `GET /v1/metrics?actor=US`
- `POST /v1/policy/evaluate`

## Strategic Use
Auracelle Charlie is designed as a **Strategic Cognitive Decision Science Engine**
for stress-testing AI governance and other frontier-technology policies.
Outputs are exploratory signals, not predictive forecasts.

## License
Research and demonstration use. Attribution required.
