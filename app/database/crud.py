from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models import URLs


class URLsCrudManager:
    @staticmethod    
    async def add_url_to_db(url: str, slug: str | None, session: AsyncSession) -> URLs:
        new_record = URLs(url=url, slug=slug)
        session.add(new_record)
        await session.commit()
        await session.refresh(new_record)
        return new_record
    
    @staticmethod
    async def get_url_by_slug(slug: str, session: AsyncSession) -> URLs | None:
        stmt = select(URLs).where(URLs.slug == slug)
        res = await session.execute(stmt)
        return res.scalar_one_or_none()
    
    @staticmethod
    async def search_url(url: str, session: AsyncSession) -> URLs | None:
        stmt = select(URLs).where(URLs.url == url)
        res = await session.execute(stmt)
        return res.scalar_one_or_none()
    
    @staticmethod
    async def check_slug_exists(slug: str, session: AsyncSession) -> bool:
        stmt = select(URLs).where(URLs.slug == slug)
        res = await session.execute(stmt)
        return res.scalar_one_or_none() is not None
