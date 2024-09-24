from fastapi.responses import JSONResponse
from ..database.redis import RedisClient
import json


def cache_response(endpoint: str, cache_time: int = 60):
    def decorator(func):
        async def wrapper(*args, **kwargs):
            redis_client = RedisClient()
            item_key = f"{endpoint}:page_{args[0]}:size_{args[1]}"

            if len(args) > 2:
                additional_params = args[2]  # args[2]'yi kwargs olarak varsayıyoruz
                item_key += ":" + ":".join(
                    [f"{key}_{value}" for key, value in additional_params.items()]
                )

            if kwargs:
                item_key += ":" + ":".join(
                    [f"{key}_{value}" for key, value in kwargs.items()]
                )

            cached_item = redis_client.get(item_key)
            if cached_item:
                return JSONResponse(content=json.loads(cached_item))

            response = await func(*args, **kwargs)
            json_response = json.dumps(response, default=str)
            redis_client.set(item_key, json_response, expire_time=cache_time)

            return response

        return wrapper

    return decorator
