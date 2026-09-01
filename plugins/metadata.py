from pyrogram import Client, filters
from helper.database import db

@Client.on_message(filters.private & filters.command("metadata"))
async def metadata_handler(c, m):
    await m.reply_text(
        "**📝 Custom Metadata**\n\n"
        "Send like:\n`title: My Video`\n\n"
        "Commands:\n"
        "/set_metadata - Save\n"
        "/see_metadata - See saved\n"
        "/del_metadata - Delete"
    )

@Client.on_message(filters.private & filters.command("set_metadata"))
async def set_metadata_cmd(c, m):
    if len(m.command) == 1:
        return await m.reply("Example: `/set_metadata title: CodeRip Encodes`")
    meta = m.text.split(None, 1)[1]
    await db.set_metadata(m.from_user.id, meta)
    await m.reply(f"✅ Saved: `{meta}`")

@Client.on_message(filters.private & filters.command("see_metadata"))
async def see_metadata_cmd(c, m):
    meta = await db.get_metadata(m.from_user.id)
    await m.reply(f"Your Metadata:\n`{meta}`" if meta else "No metadata set")

@Client.on_message(filters.private & filters.command("del_metadata"))
async def del_metadata_cmd(c, m):
    await db.set_metadata(m.from_user.id, "")
    await m.reply("🗑️ Metadata deleted")
