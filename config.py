import os
import logging
from logging.handlers import RotatingFileHandler

settings = {
    '_id': 1,  # don't change this line only, if you do you're dying by my hand
    "SPOILER": True,  # bool write True or False
    "FILE_AUTO_DELETE": 60,  # in seconds
    "AUTO_DEL": True,  # bool write True or False
    "STICKER_ID": "CAACAgUAAxkBAAIB3meeG4m-7zElzOx2KDpYgaalGpu2AAL5BgACathJVDHDY5nXgyRJHgQ",
    "stk_del_timer": 1, # in seconds
    "bot_admin": [183298628,932987382] #e.g. 1963929292,38739292827 differetiate admins with a comma
}

HELP_MSG = """help msg
"""  # shown only to admins

# Bot token @Botfather
TG_BOT_TOKEN = '6944565115:AAEA30OWWncddbFkF9FYqCykOOUb-loHyA8'
# Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "7713526"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "6f87b351ddf6c8c56999f8ba5b19cc7c")

# Your db channel Id
DB_CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001927336862"))

# NAME OF OWNER
OWNER = os.environ.get("OWNER", "yours truely")

# OWNER ID
OWNER_ID = 5071463525

# SUDO: those who can edit admins in channel
SUDO = [5071463525]
if OWNER_ID not in SUDO:
    SUDO.append(OWNER_ID)

# Port
PORT = os.environ.get("PORT", "8108")

# Database
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://alphonsemetaln:RfEJA4rlD4MdfJaU@cluster0.6evqe.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "Clustre")

# FSUBS configuration
FSUBS = [
    {'_id': -1001580437794, "CHANNEL_NAME": "Manga Yugen"}
]


TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

# Start message
START_MSG = os.environ.get("START_MESSAGE", "<blockquote><b>ʏᴏᴏ {mention} ✌🏻</b></blockquote> <blockquote>ꜱᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ ᴡɪᴛʜ ᴛʜᴇ ʟɪɴᴋꜱ ᴘʀᴏᴠɪᴅᴇᴅ ɪɴ ᴛʜᴇ ᴄʜᴀɴɴᴇʟ</blockquote>")
ADMINS = [5071463525]
# Add other admin IDs here as needed, ensuring not to include OWNER_ID
other_admin_ids = []  # Replace with actual admin IDs
for admin_id in other_admin_ids:
    if admin_id != OWNER_ID:
        ADMINS.append(admin_id)

# Ensure OWNER_ID is not duplicated
if OWNER_ID not in ADMINS:
    ADMINS.append(OWNER_ID)

# Set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = '<blockquote expandable><b>{previouscaption} \n \n◦ ʙʏ ⌯ @Anime_Yugen \n \n◦ ɴᴇᴛᴡᴏʀᴋ ⌯ @YugenNetwork</b></blockquote>'

# Set True if you want to prevent users from forwarding files from the bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

# Set true if you want to disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = True  # True or None

BOT_STATS_TEXT = "<blockquote><b>BOT UPTIME</b>\n{uptime}</blockquote>"
USER_REPLY_TEXT = "ʙᴀᴋᴋᴀ ! ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ꜱᴇɴᴘᴀɪ!!"

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
