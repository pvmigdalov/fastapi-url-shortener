from typing import Annotated

from pydantic import AnyHttpUrl, BaseModel


class ShortURLCreate(BaseModel):
    url: Annotated[str, AnyHttpUrl]