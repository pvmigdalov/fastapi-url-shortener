from datetime import datetime, timezone

from sqlalchemy import func, DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        server_default=func.now(),
        nullable=False
    )

class URLs(Base):
    __tablename__ = "urls"

    url: Mapped[str] = mapped_column(nullable=False)
    slug: Mapped[str] = mapped_column(nullable=False, unique=True, index=True)