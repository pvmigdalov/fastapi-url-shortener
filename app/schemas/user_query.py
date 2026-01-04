from typing import Annotated

from pydantic import AnyHttpUrl, BaseModel, Field


class ShortURLCreate(BaseModel):
    url: AnyHttpUrl
    slug: Annotated[
        str | None, 
        Field(
            None, 
            pattern=r"^[a-zA-Z0-9\-_]+$",
            min_length=3,
            max_length=20,
        )
    ]