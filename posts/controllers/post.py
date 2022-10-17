from typing import Any, Dict

from beanie import PydanticObjectId
from models.post import Post


class PostController:
    async def create_post(self, details: dict[str, Any]) -> bool:
        try:
            post = Post(**details)
            await post.insert()
        except Exception as e:
            print(e)
            return None
        return post

    async def update_post(self, id: PydanticObjectId, details: dict[str, Any]) -> bool:
        try:
            post = await Post.get(id)
            await post.set({**details})
        except Exception as e:
            return None
        return post

    async def delete_post(self, id: PydanticObject) -> bool:
        try:
            post = await Post.get(id)
            await post.delete()
        except Exception as e:
            return None
        return post

    async def get_all_posts(self):
        return await Post.find_all().to_list()

    async def get_post(self, id: PydanticObjectId):
        return await Post.get(id)
