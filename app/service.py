from database import Session, add_url_to_db, get_url_by_id
from utils import gen_base64_from_int, gen_int_from_base64


async def create_short_url(url: str, host: str) -> str:
    async with Session() as session:
        new_record = await add_url_to_db(url, session)
    return host + gen_base64_from_int(new_record.id)

async def get_redirect_url(b64_id: str) -> str | None:
    db_id = gen_int_from_base64(b64_id)
    async with Session() as session:
        record = await get_url_by_id(db_id, session)
    
    if not record is None:
        return record.url
    