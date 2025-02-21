from bot import Bot
import os
from pyrogram import Client, filters
from pyrogram.types import Message
from config import SUDO
from database.database import get_admins, add_bot_admin, remove_bot_admin, get_admin_ids

@Bot.on_message(filters.command("add_admin") & filters.private & filters.user(SUDO))
async def add_new_admins(client, message):
    ad_adm = message.text.split(" ")[1:]
    ad_adm = [int(admin_id) for admin_id in ad_adm]
    
    added_ids = []
    for admin_id in ad_adm:
        if add_bot_admin(admin_id):  # Add to the database
            added_ids.append(admin_id)
            await client.send_message(chat_id=admin_id, text="You have been promoted to admin.")

    if added_ids:
        OUT = f"Added {added_ids} to the admin list"
    else:
        OUT = "No new admins were added; they may already exist in the list."
    
    await client.reply_text(OUT, quote=True)

@Bot.on_message(filters.command("rm_admin") & filters.private & filters.user(SUDO))
async def remove_old_admins(client, message):
    rm_adm = message.text.split(" ")[1:]
    rm_adm = [int(admin_id) for admin_id in rm_adm]
    
    removed_ids = []
    not_found_ids = []
    for admin_id in rm_adm:
        if remove_bot_admin(admin_id):  # Remove from the database
            removed_ids.append(admin_id)
            await client.send_message(chat_id=admin_id, text="You have been demoted from admin.")
 
        else:
            not_found_ids.append(admin_id)
    
    OUT = f"Removed {removed_ids} from the admin list."
    if not_found_ids:
        OUT += f" These IDs were not in the admin list: {not_found_ids}"
    
    await client.reply_text(OUT, quote=True)

@Bot.on_message(filters.command("sudo") & filters.private)
async def sudousers(client, message):
    admin_ids = await get_admin_ids()
    user_id = message.from_user.id
    if user_id in admin_ids:
        
        admin_list = await get_admins()  # Retrieve from the database
        await message.reply_text(f"Current admins: {admin_list}", quote=True)