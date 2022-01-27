#Github.com/Vasusen-code

import os
from .. import bot
from telethon import events, Button, TelegramClient

from pyrogram import idle
from main.plugins.main import Bot, userbot

st = "𝐇𝐢,\n𝐈 𝐚𝐦 @Pyrogrammers 𝐒𝐚𝐯𝐞 𝐫𝐞𝐬𝐭𝐫𝐢𝐜𝐭𝐞𝐝 𝐜𝐨𝐧𝐭𝐞𝐧𝐭 𝐛𝐨𝐭.\n𝐘𝐨𝐮 𝐜𝐚𝐧 𝐬𝐚𝐯𝐞 𝐜𝐨𝐧𝐭𝐞𝐧𝐭𝐬 𝐨𝐟 𝐛𝐨𝐭𝐡 𝐩𝐫𝐢𝐯𝐚𝐭𝐞 𝐚𝐧𝐝 𝐩𝐮𝐛𝐥𝐢𝐜 𝐜𝐡𝐚𝐧𝐧𝐞𝐥 𝐮𝐬𝐢𝐧𝐠 𝐭𝐡𝐢𝐬 𝐛𝐨𝐭.\n𝖲𝖾𝗇𝖽 𝗆𝖾 𝗆𝖾𝗌𝗌𝖺𝗀𝖾 𝗅𝗂𝗇𝗄 𝗍𝗈 𝗀𝖾𝗍 𝗌𝗍𝖺𝗋𝗍𝖾𝖽."

@bot.on(events.NewMessage(incoming=True, pattern="/start"))
async def start(event):
    await event.reply(f'{st}', 
                      buttons=[
                        [Button.url("Updates Channel", url="https://t.me/pyrogrammers"),
                         Button.url("Support Group", url="https://t.me/+7ScFy39Vckk5MWQ1")]
                    ])
    try:
        await Bot.start()
        await userbot.start()
        await idle()
    except Exception as e:
        if 'Client is already connected' in str(e):
            pass
        else:
            return

# start help Message
@bot.on(events.NewMessage(pattern="^/help$"))
async def search(event):
    await event.reply('<b><u>This is a help message will be updated soon</b></u>', parse_mode="HTML")
#end help Message

@bot.on(events.callbackquery.CallbackQuery(data="sett"))
async def sett(event):    
    Drone = event.client                    
    button = await event.get_message()
    msg = await button.get_reply_message() 
    await event.delete()
    async with Drone.conversation(event.chat_id) as conv: 
        xx = await conv.send_message("𝐒𝐞𝐧𝐝 𝐢𝐦𝐚𝐠𝐞 𝐟𝐢𝐥𝐞 𝐚𝐬 𝐫𝐞𝐩𝐥𝐲 𝐭𝐨 𝐭𝐡𝐢𝐬 𝐦𝐞𝐬𝐬𝐚𝐠𝐞 𝐭𝐨 𝐬𝐞𝐭 𝐭𝐡𝐮𝐦𝐛𝐧𝐚𝐢𝐥.")
        x = await conv.get_reply()
        if not x.media:
            xx.edit("No media found.")
        mime = x.file.mime_type
        if not 'png' in mime:
            if not 'jpg' in mime:
                if not 'jpeg' in mime:
                    return await xx.edit("𝐏𝐡𝐨𝐭𝐨 𝐧𝐨𝐭 𝐟𝐨𝐮𝐧𝐝.")
        await xx.delete()
        t = await event.client.send_message(event.chat_id, 'Trying.')
        path = await event.client.download_media(x.media)
        if os.path.exists(f'{event.sender_id}.jpg'):
            os.remove(f'{event.sender_id}.jpg')
        os.rename(path, f'./{event.sender_id}.jpg')
        await t.edit("𝐓𝐡𝐮𝐦𝐛𝐧𝐚𝐢𝐥 𝐬𝐚𝐯𝐞𝐝!")
        
@bot.on(events.callbackquery.CallbackQuery(data="remt"))
async def remt(event):  
    Drone = event.client            
    await event.edit('Trying.')
    try:
        os.remove(f'{event.sender_id}.jpg')
        await event.edit('𝐃𝐞𝐥𝐞𝐭𝐞𝐝!')
    except Exception:
        await event.edit("𝐍𝐨 𝐭𝐡𝐮𝐦𝐛𝐧𝐚𝐢𝐥 𝐅𝐨𝐮𝐧𝐝.")                        
    
    
