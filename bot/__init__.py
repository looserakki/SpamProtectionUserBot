import logging
import sys
import time
from pyrogram import Client, errors
import config
import logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


StartTime = time.time()

API_ID = config.API_ID
API_HASH = config.API_HASH
SESSION = config.SESSION

app = Client(SESSION, api_id=API_ID, api_hash=API_HASH)
