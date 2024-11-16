import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.config import Config

from src.tasks.router import router

config = Config(".env")

PROJECT_NAME = config("PROJECT_NAME")
ENVIRONMENT = config("ENVIRONMENT")
HOST = config("HOST")
PORT = int(config("PORT"))
SHOW_DOCS_ENVIRONMENT = ("local", "staging", "development")

app_configs = {"title": PROJECT_NAME}

if ENVIRONMENT not in SHOW_DOCS_ENVIRONMENT:
    app_configs["openapi_url"] = ""  # set url for docs as empty string

app = FastAPI(**app_configs)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost",
        "http://localhost:8000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def home():
    return {
        "success": True,
        "message": "Welcome to the Another FastAPI Template by Jose Cerrejon!",
    }


app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("main:app", host=HOST, port=PORT, reload=True)
