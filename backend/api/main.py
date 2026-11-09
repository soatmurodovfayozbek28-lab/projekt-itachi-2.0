from fastapi import FastAPI
from pydantic import BaseModel

from backend.core.brain import itachi

app = FastAPI(
    title="PROJECT ITACHI 2.0",
    version="2.0.0"
)


class TaskRequest(BaseModel):
    task: str


@app.get("/")
def home():
    return {
        "project": "PROJECT ITACHI 2.0",
        "status": "ONLINE"
    }


@app.get("/status")
def status():
    return itachi.get_status()


@app.post("/think")
def think(request: TaskRequest):
    return itachi.think(request.task)