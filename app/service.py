from typing import Literal

from sqlalchemy.ext.asyncio import AsyncSession

from app.crud import URLsCrudManager
from app.exceptions import SlugAlreadyExists


async def create_short_url(
    url: str, 
    slug: str | None, 
    host: str, 
    session: AsyncSession
) -> dict[Literal["short_url", "slug"], str]:
    if slug: 
        if await URLsCrudManager.check_slug_exists(slug, session):
            raise SlugAlreadyExists
    
    record = await URLsCrudManager.add_url_to_db(url, slug, session)
    return {
        "short_url": host + record.slug,
        "slug": record.slug
    }

async def get_redirect_url(slug: str, session: AsyncSession) -> str | None:
    record = await URLsCrudManager.get_url_by_slug(slug, session)
    if record is not None:
        return record.url
    