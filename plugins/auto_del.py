from bot import Bot
from database.database import edit_auto_del, edit_file_auto_del, get_admins, get_admin_ids
import os
from pyrogram import Client, filters
from pyrogram.types import Message
from config import settings, SUDO, ADMINS


@Bot.on_message(filters.command("auto_del") & filters.private)
async def auto_del_option(client, message):
    admin_ids = await get_admin_ids()
    user_id = message.from_user.id
    if user_id in admin_ids:
        
        ad = await client.ask(message.chat.id, text="Send Message Yes/True/On to enable auto delete and send No/False/Off to disable auto delete")
        ad_l = ad.text.lower()
        if ad_l in ("on", "yes", "true"):
            edit_auto_del(True)
            OUT = f"Auto Delete has been enabled"
        elif ad_l in ("no", "false", "off"):
            edit_auto_del(False)
            OUT = f"Auto Delete has been disabled"
        else:
            OUT = f"Auto Delete Value has not changed"
        await message.reply_text(OUT, quote=True)
    
@Bot.on_message(filters.command("del_timer") & filters.private)
async def auto_del_timer(client, message):
    admin_ids = await get_admin_ids()
    user_id = message.from_user.id
    if user_id in admin_ids:
        adt = await client.ask(message.chat.id, text="Send Integer Value for Auto Delete Timer, should be greator than 0, value will be taken in seconds")
        adt_i = int(adt.text)
        if adt_i > 0:
            edit_file_auto_del(adt_i)
            OUT = f"Auto Delete Timer has been set to {adt_i} seconds"
        else:
            OUT = f"Auto Delete Timer should be greator than 0"
        await message.reply_text(OUT, quote=True)

