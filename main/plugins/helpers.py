#Github.com/Vasusen-code

from pyrogram import Client
from pyrogram.errors import FloodWait, BadRequest

import asyncio, subprocess, re, os, time

#Join private chat-------------------------------------------------------------------------------------------------------------

async def join(client, invite_link):
    try:
        await client.join_chat(invite_link)
        return "✅ 𝐍𝐨𝐰 𝐬𝐞𝐧𝐝 𝐲𝐨𝐮𝐫 𝐦𝐞𝐬𝐬𝐚𝐠𝐞 𝐥𝐢𝐧𝐤."
    except BadRequest:
        return "𝐒𝐨𝐦𝐞𝐭𝐡𝐢𝐧𝐠 𝐰𝐞𝐧𝐭 𝐰𝐫𝐨𝐧𝐠. 𝐈 𝐠𝐮𝐞𝐬𝐬 𝐲𝐨𝐮𝐫 𝐥𝐢𝐧𝐤 𝐢𝐬 𝐢𝐧𝐯𝐚𝐥𝐢𝐝 𝐨𝐫 𝐞𝐱𝐩𝐢𝐫𝐞𝐝."
    except FloodWait:
        return "𝐅𝐥𝐨𝐨𝐝 𝐰𝐚𝐢𝐭 𝐞𝐫𝐫𝐨𝐫, 𝐏𝐥𝐞𝐚𝐬𝐞 𝐭𝐫𝐲 𝐚𝐠𝐚𝐢𝐧 𝐥𝐚𝐭𝐞𝐫."
    except Exception as e:
        return "𝐅𝐥𝐨𝐨𝐝 ghffharshit𝐰𝐚𝐢𝐭 𝐞𝐫𝐫𝐨𝐫, 𝐏𝐥𝐞𝐚𝐬𝐞 𝐭𝐫𝐲 𝐚𝐠𝐚𝐢𝐧 𝐥𝐚𝐭𝐞𝐫."
           
#Regex---------------------------------------------------------------------------------------------------------------
#to get the url from event

def get_link(string):
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex,string)   
    try:
        link = [x[0] for x in url][0]
        if link:
            return link
        else:
            return False
    except Exception:
        return False
    
#Screenshot---------------------------------------------------------------------------------------------------------------

async def screenshot(video, time_stamp, sender):
    if os.path.isfile(f'{sender}.jpg'):
        return f'{sender}.jpg'
    out = str(video).split(".")[0] + ".jpg"
    cmd = (f"ffmpeg -ss {time_stamp} -i {video} -vframes 1 {out}").split(" ")
    process = await asyncio.create_subprocess_exec(
         *cmd,
         stdout=asyncio.subprocess.PIPE,
         stderr=asyncio.subprocess.PIPE)
        
    stdout, stderr = await process.communicate()
    x = stderr.decode().strip()
    y = stdout.decode().strip()
    print(x)
    print(y)
    if os.path.isfile(out):
        return out
    else:
        None
        
