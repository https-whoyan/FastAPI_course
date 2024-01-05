from src.auth.models import User
from fastapi.middleware.cors import CORSMiddleware

from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi_users import FastAPIUsers

from src.auth.manager import get_user_manager
from src.auth.auth import auth_backend
from src.auth.schemas import UserRead, UserCreate

from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend

from redis import asyncio as aioredis

from src.pages.router import router as pages_router
from src.chat.router import router as chat_router
from src.test_endpoinds.router import router as test_endpoints_router
from src.operations.router import router as router_operation
from src.tasks.router import router as tasks_router

from fastapi.staticfiles import StaticFiles


#start Redis before app start
@asynccontextmanager
async def lifespan(app: FastAPI):
    redis = aioredis.from_url("redis://localhost")
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
    yield

#app initial
app = FastAPI(
    title="My App",
    lifespan=lifespan
)

# Connect Auth System
fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

# Include all routers
app.include_router(router_operation)
app.include_router(tasks_router)
app.include_router(test_endpoints_router)
app.include_router(pages_router)
app.include_router(chat_router)


# Configure static files dir
app.mount("/src/static", StaticFiles(directory="src/static"), name="static")


# Configure middleware
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://localhost:8000",
    "http://127.0.0.1:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=["Content-Type", "Set-Cookie", "Access-Control-Allow-Headers",
                   "Access-Control-Allow-Origin", "Authorization"],
)
