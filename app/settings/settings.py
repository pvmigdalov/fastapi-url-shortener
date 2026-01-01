import os
from dotenv import load_dotenv


load_dotenv("app/settings/config.env")

class Settings:
    db_url: str = os.getenv("DATABASE_URL")