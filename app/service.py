from sqlalchemy.ext.asyncio import AsyncSession

from database import add_url_to_db, get_url_by_id
from utils import gen_base64_from_int, gen_int_from_base64


async def create_short_url(url: str, slug: str | None, host: str, session: AsyncSession) -> str:
    new_record = await add_url_to_db(url, slug, session)
    return host + new_record.slug
    # return host + gen_base64_from_int(new_record.id)

async def get_redirect_url(b64_id: str, session: AsyncSession) -> str | None:
    db_id = gen_int_from_base64(b64_id)
    record = await get_url_by_id(db_id, session)
    
    if not record is None:
        return record.url
    