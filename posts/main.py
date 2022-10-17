from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from posts.config import settings
from posts.config.db import db_connect

# from app.routers import auth, user, post

app = FastAPI()

# origins = [
#     settings.CLIENT_ORIGIN,
# ]

app.add_middleware(
    CORSMiddleware,
    # allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# app.include_router(auth.router, tags=['Auth'], prefix='/api/auth')
# app.include_router(user.router, tags=['Users'], prefix='/api/users')
# app.include_router(post.router, tags=['Posts'], prefix='/api/posts')


@app.on_event("startup")
async def start_db():
    await db_connect()


@app.get("/")
def root():
    return {"message": "Welcome to FastAPI with MongoDB"}
