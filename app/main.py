from typing import Annotated

from fastapi import FastAPI, Request, Body, Depends
from fastapi.responses import HTMLResponse

import uvicorn

from schemas import ShortURLCreate

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def welcome():
    return "<h1>Welcome to app</h1>"

@app.post("/short_url")
async def create_short_url(req: Request, url: Annotated[ShortURLCreate, Body(...)]) -> ShortURLCreate:
    print(req.base_url)
    return ShortURLCreate(
        url="http://test.test"
    )

@app.get("/{id}")
async def redirect_to(id: int):
    pass


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8001,
        reload=True
    )