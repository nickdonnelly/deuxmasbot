import os

from dotenv import load_dotenv

load_dotenv(verbose=True)

BOT_TOKEN = os.getenv("bot_token")
