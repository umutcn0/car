import redis
from ..core.services.dynaconf import settings
import json

__all__ = ["RedisClient"]


class RedisClient:
    def __init__(self):
        self.r = redis.Redis(
            host=settings.redis.host,
            port=settings.redis.port,
            db=1,
            password=settings.redis.password,
            decode_responses=True,
        )

    def set(self, key, value, expire_time=None):
        self.r.set(key, json.dumps(value), ex=expire_time)

    def get(self, key):
        value = self.r.get(key)
        return json.loads(value) if value else None

    def exists(self, key):
        return self.r.exists(key)
