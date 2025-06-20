# Flight Scraper API

## Description
An API that scrapes flight data from FlightStats and stores it in a database.
Includes background scraping with Celery and caching with Redis.

## How to Run

1. Install Redis and start the server
2. Create virtual environment & install dependencies:
   ```bash
   pip install -r requirements.txt
3. Start FastAPI:
   ```bash
   uvicorn app.main:app --reload
4. Start Celery worker:
   ```bash
   celery -A app.celery_worker.celery_app worker --loglevel=info

Testing:

```bash
pytest