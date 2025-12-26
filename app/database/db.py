from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from settings import Settings


engine = create_async_engine(Settings.db_url, echo=True)
Session = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

async def get_db_session():
    async with Session() as session:
        yield session