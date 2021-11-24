from pyrogram import idle, Client
from bot import app
from bot.modules import (
    help,
    ping,
    spb,
)


app.start()
idle()
