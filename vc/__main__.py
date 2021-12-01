from pyrogram import Client
from pytgcalls import GroupCallFactory as gcf

import vc.config

# Plugins
vsb = dict(root="vc/plugins")

# Pyro Client
app = Client(
    vc.config.SESSION_NAME,
    api_id=vc.config.API_ID,
    api_hash=vc.config.API_HASH,
    plugins=vsb,
)
bot = Client(
    "bot",
    api_id=vc.config.API_ID,
    api_hash=vc.config.API_HASH,
    bot_token=vc.config.BOT_TOKEN,
    plugins=vsb,
)


bot = bot(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="vc.plugins"),
)

bot.start()
run()


# Help Text

HELP = """** Here is a list of commands for Video Streaming Bot**
/vplay - To Stream a Video in Group ( Youtube Search, Youtube Link)
/vtelegram - To Stream a Telegram Video
/vstop - To Stop a Video Stream
/vpause - To Pause a Video Stream
/vresume - To Resume Video Stream
/vskip - To Skip The Current Playing Video
/repo - To Get The Repo
/help , /start - To Get Welcome Menu and Commands (works in private)
/alive - To Check If The Bot Is Alive"""
