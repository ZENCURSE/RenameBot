"""
Apache License 2.0
Copyright (c) 2022 @PYRO_BOTZ

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Telegram Link : https://t.me/codeflix_bots 
Repo Link : https://github.com/Codeflix-Bots/RenameBot
License Link : https://github.com/Codeflix-Bots/RenameBot/blob/main/LICENSE
"""

import random
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply, CallbackQuery
from helper.database import db
from config import Config, Txt  

@Client.on_message(filters.private & filters.command("start"))
async def start(client, message):
    user = message.from_user
    await db.add_user(client, message)                
    button = InlineKeyboardMarkup([[
        InlineKeyboardButton("👨‍💻 Dᴇᴠꜱ 👨‍💻", callback_data='dev')
        ],[
        InlineKeyboardButton('📯 Uᴩᴅᴀᴛᴇꜱ', url='https://t.me/CodeRips'),
        InlineKeyboardButton('💁‍♂️ Sᴜᴩᴩᴏʀᴛ', url='https://t.me/Code_Rips_support_bot')
        ],[
        InlineKeyboardButton('🎛️ Aʙᴏᴜᴛ', callback_data='about'),
        InlineKeyboardButton('🛠️ Hᴇʟᴩ', callback_data='help')
    ]])
    if Config.START_PIC:
        await message.reply_photo(Config.START_PIC, caption=Txt.START_TXT.format(user.mention), reply_markup=button)       
    else:
        await message.reply_text(text=Txt.START_TXT.format(user.mention), reply_markup=button, disable_web_page_preview=True)

@Client.on_callback_query(filters.regex("^(start|help|about|dev|close|CodeRips)$"))
async def cb_handler(client, query: CallbackQuery):
    data = query.data 
    try:
        if data == "start":
            btn = InlineKeyboardMarkup([[
                InlineKeyboardButton("👨‍💻 Dᴇᴠꜱ 👨‍💻", callback_data='dev')
                ],[
                InlineKeyboardButton('📯 Uᴩᴅᴀᴛᴇꜱ', url='https://t.me/CodeRips'),
                InlineKeyboardButton('💁‍♂️ Sᴜᴩᴩᴏʀᴛ', url='https://t.me/Code_Rips_support_bot')
                ],[
                InlineKeyboardButton('🎛️ Aʙᴏᴜᴛ', callback_data='about'),
                InlineKeyboardButton('🛠️ Hᴇʟᴩ', callback_data='help')
            ]])
            # FIX: handle photo message
            if query.message.photo:
                await query.message.edit_caption(caption=Txt.START_TXT.format(query.from_user.mention), reply_markup=btn)
            else:
                await query.message.edit_text(text=Txt.START_TXT.format(query.from_user.mention), disable_web_page_preview=True, reply_markup=btn)

        elif data == "help":
            btn = InlineKeyboardMarkup([[
                InlineKeyboardButton("≛ ᴏᴡɴᴇʀ", url="https://t.me/ZENCURSE")
                ],[
                InlineKeyboardButton("🧐 ʀᴇᴘᴏʀᴛ ᴀʙᴜꜱᴇ", url='https://t.me/Code_Rips_support_bot')
                ],[
                InlineKeyboardButton("✗ Cʟᴏꜱᴇ", callback_data = "close"),
                InlineKeyboardButton("« Bᴀᴄᴋ", callback_data = "start")
            ]])
            if query.message.photo:
                await query.message.edit_caption(caption=Txt.HELP_TXT, reply_markup=btn)
            else:
                await query.message.edit_text(text=Txt.HELP_TXT, disable_web_page_preview=True, reply_markup=btn)

        elif data == "about":
            btn = InlineKeyboardMarkup([[
                InlineKeyboardButton("ᴏᴜʀ ʙᴏᴛꜱ", callback_data = "CodeRips")
                ],[
                InlineKeyboardButton("✗ Cʟᴏꜱᴇ", callback_data = "close"),
                InlineKeyboardButton("Developer", callback_data = "dev")
            ]])
            if query.message.photo:
                await query.message.edit_caption(caption=Txt.ABOUT_TXT.format(client.mention), reply_markup=btn)
            else:
                await query.message.edit_text(text=Txt.ABOUT_TXT.format(client.mention), disable_web_page_preview=True, reply_markup=btn)

        elif data == "dev":
            btn = InlineKeyboardMarkup([[
                InlineKeyboardButton("≛ ᴏᴡɴᴇʀ", url="https://t.me/ZENCURSE")
                ],[
                InlineKeyboardButton("🧐 ʀᴇᴘᴏʀᴛ ᴀʙᴜꜱᴇ", url='https://t.me/Code_Rips_support_bot')
                ],[
                InlineKeyboardButton("✗ Cʟᴏꜱᴇ", callback_data = "close"),
                InlineKeyboardButton("« Bᴀᴄᴋ", callback_data = "start")
            ]])
            if query.message.photo:
                await query.message.edit_caption(caption=Txt.DEV_TXT, reply_markup=btn)
            else:
                await query.message.edit_text(text=Txt.DEV_TXT, disable_web_page_preview=True, reply_markup=btn)

        elif data == "close":
            try:
                await query.message.delete()
                if query.message.reply_to_message:
                    await query.message.reply_to_message.delete()
            except:
                try:
                    await query.message.delete()
                except:
                    pass
    except Exception as e:
        print(f"Callback error: {e}")
