from pydantic import AnyHttpUrl, BaseModel


class ShortURLCreate(BaseModel):
    url: AnyHttpUrl