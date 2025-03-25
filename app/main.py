from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Mount static files directory
app.mount("/static", StaticFiles(directory="app/static"), name="static")


@app.get("/")
async def root():
    return {"message": "Hello from FastAPI!"}


@app.get("/favicon.ico")
async def favicon():
    return FileResponse("app/static/favicon.ico")
