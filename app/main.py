from fastapi import FastAPI
from fastapi.responses import HTMLResponse

import uvicorn

from schemas import ShortURLCreate

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def welcome():
    return "<h1>Welcome to app</h1>"

@app.post("/short_url")
async def create_short_url(url: ShortURLCreate) -> ShortURLCreate:
    return ShortURLCreate(
        url="http://test.test"
    )

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8001,
        reload=True
    )