# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01

from pyrogram import Client, types
from info import *
from aiohttp import web

TechVJBackUpBot = Client(SESSION, api_id=API_ID, api_hash=API_HASH, bot_token=BACKUP_BOT_TOKEN)

class TechVJXBot(Client):

    def __init__(self):
        super().__init__(
            name=SESSION,
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            workers=150,
            plugins={"root": "plugins"},
            sleep_threshold=5,
        )
      
TechVJBot = TechVJXBot()

multi_clients = {}
work_loads = {}
