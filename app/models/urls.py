from datetime import datetime, timezone
from functools import partial

from sqlalchemy import DateTime, String, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


nowutc = partial(datetime.now, timezone.utc)

class Base(DeclarativeBase):
    created_at: Mapped[datetime] = mapped_column(
        default=nowutc,
        server_default=func.now(),
        nullable=False
    )

class Urls(Base):
    __tablename__ = "urls"

    url_in: Mapped[str] = mapped_column(unique=True, nullable=False)
    url_out: Mapped[str] = mapped_column(unique=True, nullable=False)