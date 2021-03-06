import asyncio

from pyrogram import filters

from .. import bot
from ..functions import (admin_check, user_input, video_stream,
                         youtube_stream)

que = asyncio.Queue()
number = 0
loop = asyncio.get_event_loop()


# Stream A Video From Youtube/Telegram


@bot.on_message(
    filters.command(["vplay", "vtelegram"])
)
async def stream(client, message):
    reply = message.reply_to_message
    user_str = await user_input(message.text)
    if message.command[0][1] == "p" and not user_str:
        return await message.reply(
            "Please give a youtube link/keyword or reply /vtelegram to a valid video to stream!"
        )
    if message.command[0][1] == "t":
        if not (reply and reply.video):
            return await message.reply(
                "Please give a youtube link/keyword or reply /vtelegram to a valid video to stream!"
            )
        download_ = await message.reply("Downloading The Replied Video!")
        video = await reply.download(file_name="DOWNLOADS/")
        await download_.delete()
    if Calls.is_running:
        if user_str:
            next_vid = user_str
        else:
            next_vid = video
        await que.put(next_vid)
        global number
        number += 1
        content = user_str if user_str else "Telegram Video"
        return await message.reply(
            f"Added **Video🎥** : **__{content}__** To Queue!\n\n**Queued at #{number}**"
        )
    try:
        invideo = user_str if user_str else video
        await video_stream(chat_id, invideo, client, message)
    except Exception as e:
        return await message.reply(e)


# Stop Video Chat


@bot.on_message(filters.command("vstop"))
async def stop(client, message):
    if not Calls.is_running:
        return await message.reply("No Stream Going On!")
    global number
    admins = await admin_check(client, message)
    if message.from_user.id not in admins:
        return await message.reply(
            "You Dont Have Sufficient Permissions!,(Manage Video Chats)"
        )
    await Calls.stop()
    number = 0
    que._queue.clear()
    return await message.reply("The Video Has Been Stopped Successfully!")


# Skip Video Stream


@bot.on_message(filters.command("vskip"))
async def skip(client, message):
    global number
    admins = await admin_check(client, message)
    if message.from_user.id not in admins:
        return await message.reply(
            "You Dont Have Sufficient Permissions!,(Manage Video Chats)"
        )
    if que.empty():
        await message.reply("No More Videos In Queue!\nLeaving Video Chat!")
        return await Calls.stop()
    else:
        stuff = await que.get()
        number -= 1
    try:
        await video_stream(chat_id, stuff, client, message)
    except Exception as e:
        return await message.reply(e)


# 
