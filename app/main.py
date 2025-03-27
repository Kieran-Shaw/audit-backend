from functools import lru_cache

from fastapi import FastAPI
from fastapi.responses import FileResponse
from starlette.staticfiles import StaticFiles

app = FastAPI(
    title="Audit Backend API",
    description="Python and FastAPI backend for audit",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# Mount static files directory
app.mount("/static", StaticFiles(directory="app/static"), name="static")


@app.get("/", response_model=dict[str, str])
async def root() -> dict[str, str]:
    return {"message": "Hello from FastAPI!"}


@lru_cache(maxsize=1)
def get_favicon() -> str:
    return "app/static/favicon.ico"


@app.get("/favicon.ico", response_class=FileResponse)
async def favicon() -> FileResponse:
    return FileResponse(
        get_favicon(),
        media_type="image/x-icon",
        content_disposition_type="inline"
    )
