from typing import Literal

from sqlalchemy.ext.asyncio import AsyncSession

from database import URLsCrudManager
from exceptions import SlugAlreadyExists
# from utils import gen_base64_from_int, gen_int_from_base64


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
    # return host + gen_base64_from_int(new_record.id)

async def get_redirect_url(slug: str, session: AsyncSession) -> str | None:
    # db_id = gen_int_from_base64(b64_id)
    record = await URLsCrudManager.get_url_by_slug(slug, session)
    if record is not None:
        return record.url
    