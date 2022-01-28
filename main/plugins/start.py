#Github.com/Vasusen-code

import os
from .. import bot
from telethon import events, Button, TelegramClient

from pyrogram import idle
from main.plugins.main import Bot, userbot

st = "**Hii,\nI am @Pyrogrammers Save restricted Contents bot.**\nSend me any public or private restricted Channel post link.\nI will give you that post.\n**Hit /help to know more.**"

@bot.on(events.NewMessage(incoming=True, pattern="/start"))
async def start(event):
    await event.reply(f'{st}', 
                      buttons=[
                        [Button.url("Updates Channel", url="https://t.me/pyrogrammers"),
                         Button.url("Support Group", url="https://t.me/+7ScFy39Vckk5MWQ1")],
                        [Button.url("YouTube Channel", url="https://youtube.com/channel/UC2anvk7MNeNzJ6B4c0SZepw")],
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
    await event.reply('<b><u>For Public Restricted Channel contents.</b></u>\nTo get public restricted Channel contents, just send your Post link i will give you that post without Downloading.\n\n<b><u>For Private Restricted Channel contents.</b></u>\nTo get private restricted Channel contents, First send me Channel invite link so that i can join your channel after that send me post link of your restricted Channel to get that post.', parse_mode="HTML")
#end help Message

@bot.on(events.NewMessage(pattern="/setthumb"))
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
        
@bot.on(events.NewMessage(pattern="/delthumb"))
async def remt(event):  
    Drone = event.client            
    await event.edit('Trying.')
    try:
        os.remove(f'{event.sender_id}.jpg')
        await event.edit('𝐃𝐞𝐥𝐞𝐭𝐞𝐝!')
    except Exception:
        await event.edit("𝐍𝐨 𝐭𝐡𝐮𝐦𝐛𝐧𝐚𝐢𝐥 𝐅𝐨𝐮𝐧𝐝.")                        
    
    
