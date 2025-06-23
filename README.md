# ✈️ Flight Info API

[![Python](https://img.shields.io/badge/python-3.9%2B-blue)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-async%20web%20framework-green)](https://fastapi.tiangolo.com/)
[![Celery](https://img.shields.io/badge/Celery-Task%20Queue-%23E0004D)](https://docs.celeryq.dev/en/stable/)
[![Redis](https://img.shields.io/badge/Redis-Caching-red)](https://redis.io/)


## 🚀 Overview

This API provides real-time flight information scraped from FlightStats, backed by FastAPI, Celery, Redis, and SQLAlchemy.

## 📦 Features

- 🔍 Flight info by airline code, number, and date
- ⚙️ Celery background job processing
- ⚡ Redis caching
- 💾 SQLAlchemy ORM
- 🧪 Pytest-based test suite

## 🛠️ Setup

```bash
git clone https://github.com/imohammedzohaib/flight_api.git
cd flight_api
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

📡 Run Services

# Start Redis
redis-server

# Start Celery
celery -A celery_worker.celery worker --loglevel=info

# Run FastAPI app
uvicorn app.main:app --reload

✅ Example:
GET /flight-info?airline_code=AA&flight_number=100&departure_date=2025-06-25

🧪 Run Tests:
```bash
pytest


📂 Folder Structure

flight_api/
├── app/
│   ├── api/v1/
│   ├── cache/
│   ├── core/
│   ├── db/
│   ├── models/
│   ├── schemas/
│   ├── services/
│   ├── tasks/
│   └── main.py
├── tests/
├── celery_worker.py
├── requirements.txt
└── README.md
