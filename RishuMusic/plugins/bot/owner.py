from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from RishuMusic import app
from config import BOT_USERNAME
from RishuMusic.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """
**
┌┬─────────────────⦿
│├─────────────────╮
│├ ᴛɢ ɴᴀᴍᴇ - 𝐇єᴧʀ፝֠֩ᴛʙєᴧᴛ
│├ ʀᴇᴀʟ ɴᴀᴍᴇ -𝐇єᴧʀ፝֠֩ᴛʙєᴧᴛ
│├─────────────────╯
├┼─────────────────⦿
├┤~ @UFC_UPDATES
├┤~ @ll_P_U_L_lI
├┼─────────────────⦿
│├─────────────────╮
│├OWNER│ @l_HEART_BEAT_l
│├─────────────────╯
└┴─────────────────⦿
**
"""




@app.on_message(filters.command("owner"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton(" 𝐇єᴧʀ፝֠֩ᴛʙєᴧᴛ ", url=f"https://t.me/l_HEART_BEAT_l")
        ],
        [
          InlineKeyboardButton("ＨＥＬＰ", url="https://t.me/UFC_UPDATES"),
          InlineKeyboardButton("ＲＥＰＯ", url="https://t.me/TAMANNA_MUSIC_BOT?start=_tgr_fBSoVjdmODhl"),
          ],
               [
                InlineKeyboardButton(" ＮＥＴＷＯＲＫ", url=f"https://t.me/UFC_UPDATES"),
],
[
InlineKeyboardButton("ＯＦＦＩＣＩＡＬ ＢＯＴ", url=f"https://t.me/TAMANNA_MUSIC_BOT"),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://files.catbox.moe/kzl8vt.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
