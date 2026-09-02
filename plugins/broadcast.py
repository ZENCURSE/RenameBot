from pyrogram import Client, filters
from config import Config
from helper.database import db
import asyncio

ADMIN = Config.ADMIN if hasattr(Config, 'ADMIN') else getattr(Config, 'ADMINS', [])

@Client.on_message(filters.command("broadcast") & filters.private & filters.user(ADMIN))
async def broadcast(bot, message):
    if message.reply_to_message:
        users = await db.get_all_users()
        b_msg = message.reply_to_message
        sts = await message.reply_text("Broadcasting...")
        total = 0
        success = 0
        async for user in users:
            total += 1
            try:
                await b_msg.copy(chat_id=int(user['id']))
                success += 1
                await asyncio.sleep(0.5)
            except:
                pass
        await sts.edit(f"**Broadcast Done**\nTotal: {total}\nSuccess: {success}")
    else:
        await message.reply_text("Reply to any message to broadcast")

@Client.on_message(filters.command("users") & filters.private & filters.user(ADMIN))
async def get_users(bot, message):
    count = await db.total_users_count()
    await message.reply_text(f"Total Users: {count}")
