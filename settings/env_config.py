import os
from dotenv import load_dotenv

load_dotenv()


class EnvConfig:
    SECRET_KEY = os.getenv("CONFIG__SECRET_KEY")

    DATABASE_URL = os.getenv("CONFIG__DATABASE_URL")
