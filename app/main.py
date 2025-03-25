from fastapi import FastAPI
from fastapi.responses import FileResponse
from starlette.staticfiles import StaticFiles

app = FastAPI()

# Mount static files directory
app.mount("/static", StaticFiles(directory="app/static"), name="static")


@app.get("/", response_model=dict[str, str])
async def root() -> dict[str, str]:
    return {"message": "Hello from FastAPI!"}


@app.get("/favicon.jpg", include_in_schema=False)
async def favicon():
    return FileResponse("app/static/favicon.jpg")
