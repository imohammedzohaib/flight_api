import redis
import json

redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

def get_cached_flight(key):
    data = redis_client.get(key)
    if data:
        return json.loads(data)
    return None

def set_cached_flight(key, data, expiration=3600):
    redis_client.setex(key, expiration, json.dumps(data))