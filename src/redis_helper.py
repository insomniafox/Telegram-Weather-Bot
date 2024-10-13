import redis.asyncio as redis

redis_client = redis.from_url("redis://redis")


async def set_user_language(user_id: str | int, language: str):
    await redis_client.set(f"user:{user_id}:language", language)


async def get_user_language(user_id: str | int) -> str:
    language = await redis_client.get(f"user:{user_id}:language")
    return language.decode('utf-8') if language else 'ru'
