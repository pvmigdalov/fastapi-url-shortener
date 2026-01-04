from typing import Annotated

from pydantic import AnyHttpUrl, BaseModel, Field


class ShortURLCreate(BaseModel):
    url: AnyHttpUrl
    #slug: Annotated[str, Field(None, pattern=r"^[a-zA-Z0-9\-_]+$")]