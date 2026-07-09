from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.api.routes import router

app = FastAPI(
    title="AI Response Quality Evaluation System",
    description="A RAG-based system for evaluating AI-generated responses using reference knowledge.",
    version="1.0.0"
)

app.include_router(router)

app.mount(
    "/static",
    StaticFiles(directory="app/static"),
    name="static"
)