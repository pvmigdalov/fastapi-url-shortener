from typing import Annotated

from fastapi import FastAPI, Request, Body, HTTPException, status
from fastapi.responses import HTMLResponse, RedirectResponse

import uvicorn

from schemas import ShortURLCreate
from service import create_short_url, get_redirect_url

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def welcome():
    return "<h1>Welcome to app</h1>"

@app.post("/short_url")
async def get_short_url(req: Request, url: Annotated[ShortURLCreate, Body(...)]) -> ShortURLCreate:
    short_url = await create_short_url(url.url, req.base_url)
    return ShortURLCreate(url=short_url)

@app.get("/{b64_id}", status_code=status.HTTP_302_FOUND)
async def redirect_to(b64_id: str):
    redirect_url = get_redirect_url(b64_id)
    if redirect_url is None:
        raise HTTPException(status.HTTP_400_BAD_REQUEST)
    return RedirectResponse(redirect_url)


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8001,
        reload=True
    )