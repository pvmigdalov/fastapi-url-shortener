from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class URLs(Base):
    __tablename__ = "urls"

    url: Mapped[str] = mapped_column(nullable=False)
    slug: Mapped[str] = mapped_column(nullable=False, unique=True, index=True)