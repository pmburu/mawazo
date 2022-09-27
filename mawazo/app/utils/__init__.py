"""Application implementation - utilities.

Resources:
    1. https://aioredis.readthedocs.io/en/latest/

"""
from mawazo.app.utils.aiohttp_client import AiohttpClient
from mawazo.app.utils.redis import RedisClient


__all__ = ("AiohttpClient", "RedisClient")
