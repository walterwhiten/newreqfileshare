from bot import Bot
from pyrogram import Client, filters
from pyrogram.types import Message
from database.database import edit_sticker_id, get_admins, get_admin_ids
from config import settings, ADMINS, SUDO


@Bot.on_message(filters.command("add_sticker") & filters.private)
async def request_sticker(client, message):
    admin_ids = await get_admin_ids()
    user_id = message.from_user.id
    if user_id in admin_ids:
        response = await client.ask(message.chat.id, "Send a sticker, or type 'Stop' to cancel.")
        if response.sticker:
            stck_id = response.sticker.file_id
            edit_sticker_id(stck_id)
            await response.reply("Thank you for the sticker!")
        else:
            await response.reply("That's not a sticker! Process cancelled")
