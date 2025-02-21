#(©)AnimeYugen

from aiohttp import web
from plugins import web_server

import pyromod.listen
from pyrogram import Client
from pyrogram.enums import ParseMode
import sys
from datetime import datetime

from config import API_HASH, APP_ID, LOGGER, TG_BOT_TOKEN, TG_BOT_WORKERS, FSUBS, DB_CHANNEL_ID, PORT


name ="""
 BY Voat FROM TG
"""


class Bot(Client):
    def __init__(self):
        super().__init__(
            name="Bot",
            api_hash=API_HASH,
            api_id=APP_ID,
            plugins={
                "root": "plugins"
            },
            workers=TG_BOT_WORKERS,
            bot_token=TG_BOT_TOKEN
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        usr_bot_me = await self.get_me()
        self.uptime = datetime.now()
        try:
            db_channel = await self.get_chat(DB_CHANNEL_ID)
            self.db_channel = db_channel
            test = await self.send_message(chat_id = db_channel.id, text = "Testing Message by @VOATcb")
            await test.delete()
        except Exception as e:
            self.LOGGER(__name__).warning(e)
            self.LOGGER(__name__).warning(f"Make Sure bot is Admin in DB Channel, and Double check the DB_CHANNEL_ID Value, Current Value {DB_CHANNEL_ID}")
            self.LOGGER(__name__).info("\nBot Stopped. Join https://t.me/Yugen_Bots_Support for support")
            sys.exit()
        
        self.set_parse_mode(ParseMode.HTML)
        self.LOGGER(__name__).info(f"Bot Running..!\n\nCreated by \nhttps://t.me/VOATcb")
        self.LOGGER(__name__).info(f""" \n\n       
                                                   
                  
                                 


██╗░░░██╗██╗░░░██╗░██████╗░███████╗███╗░░██╗
╚██╗░██╔╝██║░░░██║██╔════╝░██╔════╝████╗░██║
░╚████╔╝░██║░░░██║██║░░██╗░█████╗░░██╔██╗██║
░░╚██╔╝░░██║░░░██║██║░░╚██╗██╔══╝░░██║╚████║
░░░██║░░░╚██████╔╝╚██████╔╝███████╗██║░╚███║
░░░╚═╝░░░░╚═════╝░░╚═════╝░╚══════╝╚═╝░░╚══╝

            ██████╗░░█████╗░████████╗░██████╗
            ██╔══██╗██╔══██╗╚══██╔══╝██╔════╝
            ██████╦╝██║░░██║░░░██║░░░╚█████╗░
            ██╔══██╗██║░░██║░░░██║░░░░╚═══██╗
            ██████╦╝╚█████╔╝░░░██║░░░██████╔╝
            ╚═════╝░░╚════╝░░░░╚═╝░░░╚═════╝░                                                         
 
                                                                        
                                                                      
                                                                                 
                              
                                          """)
        self.username = usr_bot_me.username
        #web-response
        app = web.AppRunner(await web_server())
        await app.setup()
        bind_address = "0.0.0.0"
        await web.TCPSite(app, bind_address, PORT).start()

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped.")
            
