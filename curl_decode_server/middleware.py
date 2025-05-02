from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

html_file_path = "./curl_decode_server/index.html"
file_path = "request_counter.txt"
request_counter: int = 0


def init_middleware(app: FastAPI) -> None:
    """Initialize middleware for the FastAPI app."""

    @app.middleware("http")
    async def count_request_and_redirect_browser(request: Request, call_next):
        global request_counter
        request_counter += 1
        if "User-Agent" not in request.headers or "curl" not in request.headers["User-Agent"]:
            with open(html_file_path, "r") as f:
                return HTMLResponse(f.read())
        response = await call_next(request)
        return response
