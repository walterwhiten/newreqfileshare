from bot import Bot
import os
from database.database import edit_spoiler, get_admins, get_admin_ids
from pyrogram import Client, filters
from pyrogram.types import Message
from config import ADMINS, SUDO, settings

@Bot.on_message(filters.command("spoiler") & filters.private)
async def image_spoiler(client, message):
    admin_ids = await get_admin_ids()
    user_id = message.from_user.id
    if user_id in admin_ids:
        spl = await client.ask(
            message.chat.id, 
            text="Do you want to show spoiler in images? Type Yes/On/True to confirm, or No/Off/False to close this message with no changes applied."
        )
        spl_l = spl.text.lower()
        
        if spl_l in ('on', 'true', 'yes'):
            edit_spoiler(True)
            OUT = "Spoiler has been set."
        elif spl_l in ('off', 'no', 'false'):
            edit_spoiler(False)
            OUT = "Spoiler has been removed."
        else:
            current_spoiler = get_spoiler()
            OUT = f"Spoiler value remains as before, i.e., {current_spoiler}."
        
        await message.reply_text(OUT, quote=True)

    