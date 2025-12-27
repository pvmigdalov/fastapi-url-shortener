from sqlalchemy import insert
from sqlalchemy.ext.asyncio import AsyncSession

from models import URLs
from utils import non_instantiable


@non_instantiable
class URLsCrudManager:
    Model = URLs

    @classmethod
    async def add_url_to_db(cls, url: str, session: AsyncSession) -> URLs:
        new_url = cls.Model(url=url)
        session.add(new_url)
        await session.commit()
        return new_url