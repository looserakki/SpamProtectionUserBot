import asyncio
from pyrogram import filters
from bot import app


@app.on_message(filters.me & filters.regex("^\.help$"))
def mainhelp(_, m):
    m.edit(infohelptext)

infohelptext = f"""
『 INFO STUFF 』
  .spb -> get info of a person from Intellivoid SpamProtection API.
  .ping -> to see bot working or not.
"""
