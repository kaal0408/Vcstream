import requests
from pyrogram import Client as Bot
from vc.config import API_HASH
from vc.config import API_ID
from vc.config import BG_IMAGE
from vc.config import BOT_TOKEN
from vc.services.callsmusic import run

response = requests.get(BG_IMAGE)
file = open("./etc/foreground.png", "wb")
file.write(response.content)
file.close()

bot = Bot(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="vc.plugins"),
)

bot.start()
run()
