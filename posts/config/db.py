from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from posts.config.settings import settings
from posts.models.post import Comment, Post


async def db_connect():
    global client
    client = AsyncIOMotorClient(f"mongodb://mongo:27017/mawazo_posts")
    await init_beanie(database=client.db_name, document_models=[Comment, Post])


async def db_disconnect():
    client.close()
