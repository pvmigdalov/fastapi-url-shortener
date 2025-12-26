import os
from dotenv import load_dotenv

load_dotenv("app/settings/config.env")

dev_mode = (os.getenv("DEV_MODE") == "true")
local_db_url = os.getenv("LOCAL_DATABASE_URL")
container_db_url = os.getenv("CONTAINER_DATABASE_URL")

class Settings:
    db_url: str = local_db_url if dev_mode else container_db_url