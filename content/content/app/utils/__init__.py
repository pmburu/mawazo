"""Application implementation - utilities.

Resources:
    1. https://aioredis.readthedocs.io/en/latest/

"""
from content.app.utils.aiohttp_client import AiohttpClient
from content.app.utils.redis import RedisClient


__all__ = ("AiohttpClient", "RedisClient")
