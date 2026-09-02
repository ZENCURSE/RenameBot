from datetime import datetime
from pytz import timezone
from pyrogram import Client, __version__
from pyrogram.raw.all import layer
from config import Config
from aiohttp import web
from route import web_server

class Bot(Client):
    def __init__(self):
        super().__init__(
            name="renamer",
            api_id=Config.API_ID,
            api_hash=Config.API_HASH,
            bot_token=Config.BOT_TOKEN,
            workers=200,
            plugins={"root": "plugins"},
            sleep_threshold=15,
            in_memory=True
        )

    async def start(self):
        await super().start()
        me = await self.get_me()
        self.mention = me.mention
        self.username = me.username  
        self.uptime = datetime.now()
        
        if getattr(Config, "WEBHOOK", False):
            app = web.AppRunner(await web_server())
            await app.setup()       
            await web.TCPSite(app, "0.0.0.0", 8080).start()     
            
        print(f"{me.first_name} Is Started.....")
        for id in Config.ADMIN:
            try: 
                await self.send_message(id, f"**{me.first_name} Is Started.....**")                                
            except: 
                pass

    async def stop(self, *args):
        await super().stop()
        print("Bot Stopped")

Bot().run()
