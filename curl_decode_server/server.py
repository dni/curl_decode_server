from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

from .ascii_art import error, not_found
from .middleware import init_middleware
from .router import router

file_path = "./request_counter.txt"
max_body_size = 2 * 1024 * 1024  # 2 MB


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator:
    with open(file_path, "r") as f:
        try:
            app.state.counter = int(f.read())
        except ValueError:
            app.state.counter = 0
    app.include_router(router)
    yield
    with open(file_path, "w") as f:
        f.write(str(app.state.counter))


app = FastAPI(lifespan=lifespan, max_request_body_size=max_body_size)

init_middleware(app)


@app.exception_handler(404)
async def not_found_exception_handler(*_) -> PlainTextResponse:
    return PlainTextResponse(not_found(app.state.counter))


@app.exception_handler(Exception)
async def exception_handler(*_) -> PlainTextResponse:
    return PlainTextResponse(error)
