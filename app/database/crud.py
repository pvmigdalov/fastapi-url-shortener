from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models import URLs


async def add_url_to_db(url: str, session: AsyncSession) -> URLs:
    new_record = URLs(url=url)
    session.add(new_record)
    await session.commit()
    return new_record

async def get_url_by_id(id: int, session: AsyncSession) -> URLs | None:
    stmt = select(URLs).where(URLs.id == id)
    res = await session.execute(stmt)
    return res.scalar()
