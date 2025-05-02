from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

from .ascii_art import not_found, error
from .router import router
from .middleware import request_counter, file_path, init_middleware

@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator:
    global request_counter
    with open(file_path, 'r') as f:
        try:
            request_counter = int(f.read())
        except ValueError:
            request_counter = 0
    app.include_router(router)
    yield
    with open(file_path, 'w') as f:
        f.write(str(request_counter))


app = FastAPI(lifespan=lifespan)

init_middleware(app)



@app.exception_handler(404)
async def not_found_exception_handler(*_) -> PlainTextResponse:
    return PlainTextResponse(not_found)


@app.exception_handler(Exception)
async def exception_handler(*_) -> PlainTextResponse:
    return PlainTextResponse(error)
