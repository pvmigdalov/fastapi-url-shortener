from typing import Annotated

from fastapi import FastAPI, Depends, Request, Body, Path, HTTPException, status
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlalchemy.ext.asyncio import AsyncSession

import uvicorn

from database import get_db_session
from schemas import ShortURLCreate
from service import create_short_url, get_redirect_url

app = FastAPI()
session_dependency = Annotated[AsyncSession, Depends(get_db_session)]

@app.get("/", response_class=HTMLResponse)
async def welcome():
    return "<h1>Welcome to app</h1>"

@app.post("/short_url")
async def get_short_url(
    req: Request, 
    url: Annotated[ShortURLCreate, Body(...)],
    session: session_dependency
) -> ShortURLCreate:
    short_url = await create_short_url(
        str(url.url),
        url.slug, 
        str(req.base_url),
        session
    )
    return ShortURLCreate(url=short_url)

@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

@app.get("/{b64_id}")
async def redirect_to(
    b64_id: Annotated[str, Path(pattern=r"^[a-zA-Z0-9\-_]+$")],
    session: session_dependency
):
    redirect_url = await get_redirect_url(b64_id, session)
    if redirect_url is None:
        raise HTTPException(status.HTTP_400_BAD_REQUEST)
    return RedirectResponse(redirect_url, status_code=status.HTTP_302_FOUND)


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8001,
        reload=True
    )