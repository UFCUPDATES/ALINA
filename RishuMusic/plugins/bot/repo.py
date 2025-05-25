from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from RishuMusic import app
from config import BOT_USERNAME
from RishuMusic.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """
**⌾ ᴡᴇʟᴄᴏᴍᴇ ғᴏʀ 𝐇єᴧʀ፝֠֩ᴛʙєᴧᴛ ʀᴇᴘᴏs ⌾
 
● ɪғ ʏᴏᴜ ᴡᴀɴᴛ ˹ αℓιиα ꭙ ᴍᴜsɪᴄ ♡゙゙

● ʙᴏᴛ ʀᴇᴘᴏ ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʀᴇᴘᴏ ● **
"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("✙ ᴀᴅᴅ ᴍᴇ ✙", url=f"https://t.me/ALINA_UFC_BOT?startgroup=true")
        ],
        [
          InlineKeyboardButton("• ʜᴇʟᴘ •", url="https://t.me/UFC_UPDATES"),
          InlineKeyboardButton("• 𝐇єᴧʀ፝֠֩ᴛʙєᴧᴛ •", url="https://t.me/l_HEART_BEAT_l"),
          ],
               [
                InlineKeyboardButton("• ɴᴇᴛᴡᴏʀᴋ •", url=f"https://t.me/UFC_UPDATES"),
],
[
InlineKeyboardButton("• ʀᴇᴘᴏ •", url=f"https://files.catbox.moe/0krfkc.jpg"),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://files.catbox.moe/kzl8vt.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
