from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from backend.core.brain import itachi

app = FastAPI(
    title="PROJECT ITACHI 2.0",
    version="2.0.0"
)


class TaskRequest(BaseModel):
    task: str = Field(min_length=1, max_length=5000)


class MemoryRequest(BaseModel):
    category: str = Field(min_length=1, max_length=100)
    content: str = Field(min_length=1, max_length=10000)


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


@app.post("/memory")
def save_memory(request: MemoryRequest):
    return itachi.remember(
        request.category,
        request.content
    )


@app.get("/memory")
def get_memories(limit: int = 20):
    if not 1 <= limit <= 100:
        raise HTTPException(
            status_code=400,
            detail="Limit must be between 1 and 100"
        )

    return itachi.recall(limit)


@app.get("/memory/search")
def search_memory(keyword: str):
    if not keyword.strip():
        raise HTTPException(
            status_code=400,
            detail="Keyword cannot be empty"
        )

    return itachi.search_memory(keyword)