import os
from dotenv import load_dotenv

load_dotenv("app/settings/config.env")

local_mode = (os.getenv("LOCAL_MODE") == "true")
local_db_url = os.getenv("LOCAL_DATABASE_URL")
container_db_url = os.getenv("CONTAINER_DATABASE_URL")

class Settings:
    db_url: str = local_db_url if local_mode else container_db_url