from datetime import datetime

from beanie import Document, Link
from pydantic import BaseModel


# Comment dataclass - connects to the comment dataclass as
# a dictionary of comment_author and comment
class Comment(Document):
    author_id: str
    comment: str
    date: datetime = datetime.now()


# Post dataclass - keeps all post attributes as optional Python 3.10
# style and takes comments as a list of dictionaries
class Post(Document):
    title: str
    image: str | None = None
    content: str
    date: datetime = datetime.now()
    tags: list[str]
    comments: list[Link[Comment]] | None = None
    loves: list[int] = None
    bookmarks: list[dict] = None

    class Settings:
        name = "post"

    class Config:
        schema_extra = {
            "example": {
                "title": "We Conquered It All",
                "image": "moon.png",
                "content": "Oh how amazing it was ...!",
                "date": datetime.now(),
                "tags": ["Travel", "Conquer"],
                "comments": None,
                "loves": None,
                "bookmarks": None,
            }
        }


# Update schema using Pydantic BaseModel class in order
# to update only fieds present in the request body
class UpdatePost(BaseModel):
    title: str | None = None
    image: str | None = None
    content: str | None = None
    date: datetime | None = None
    tags: list[str] | None = None
    comments: list[Link[Comment]] | None = None
    loves: list[int] | None
    bookmarks: list[dict] | None

    class Config:
        schema_extra = {
            "example": {
                "title": "We Conquered It All",
                "image": "moon.png",
                "content": "Oh how amazing it was ...!",
                "date": datetime.now(),
                "tags": ["Travel", "Conquerer", "Lifetime"],
                "comments": None,
                "loves": None,
                "bookmarks": None,
            }
        }
