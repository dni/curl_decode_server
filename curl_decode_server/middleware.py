from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

file_path = "request_counter.txt"
request_counter: int = 0


def init_middleware(app: FastAPI) -> None:
    """Initialize middleware for the FastAPI app."""

    @app.middleware("http")
    async def count_request_and_redirect_browser(request: Request, call_next):
        global request_counter
        request_counter += 1
        if "User-Agent" in request.headers:
            user_agent = request.headers["User-Agent"]
            if "curl" not in user_agent:
                return HTMLResponse(
                    """
                    <h1>Welcome to the dni's encoder</h1>
                    <p>Use <b>`curl dec.dni.guru`</b> to access this site.</p>
                    <p>made with ❤ by dni</p>
                    """
                )
        response = await call_next(request)
        return response
