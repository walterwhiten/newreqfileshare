#(©)Yugen_Bots

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID, HELP_MSG
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<blockquote expandable><b>┏━━━━━━━⛩️━━━━━━━┓\n× ɢᴏᴅ : <a href='tg://user?id={OWNER_ID}'>🫨 🫨</a>\n× ᴀɴɪᴍᴇ ᴄʜᴀɴɴᴇʟ : @Anime_Yugen\n× ᴍᴀɴɢᴀ ᴄʜᴀɴɴᴇʟ : @Manga_Yugen\n× ʏᴜɢᴇɴ ɴᴇᴛᴡᴏᴋ : @YugenNetwork\n┗━━━━━━━⛩️━━━━━━━┛</b></blockquote>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    
                    [
                    InlineKeyboardButton("😔 ᴄʟᴏsᴇ", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "help":
        await query.message.edit_text(
            text = HELP_MSG,
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                    InlineKeyboardButton("😔 ᴄʟᴏsᴇ", callback_data = "close")
                    ]
                ]
            )
        )
        
        
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass


