import redis
import json
from app.core.config import settings

r = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=0)

def set_cached_flight_data(key, data):
    r.set(key, json.dumps(data), ex=3600)

def get_cached_flight_data(key):
    data = r.get(key)
    return json.loads(data) if data else None
