#Github.com/Vasusen-code

from pyrogram import Client
from pyrogram.errors import FloodWait, BadRequest
#What the hell is it??
from telethon.tl.functions.users import GetFullUserRequest
from telethon.errors.rpcerrorlist import UserNotParticipantError
from telethon.tl.functions.channels import GetParticipantRequest
#end
import asyncio, subprocess, re, os, time


#remove it
#join check
async def check_user(id):
    ok = True
    try:
        await bot(GetParticipantRequest(channel='@pyrogrammers', participant=id))
        ok = True
    except UserNotParticipantError:
        ok = False
    return ok
#end


#Join private chat-------------------------------------------------------------------------------------------------------------

async def join(client, invite_link):
    ok = await bot(GetFullUserRequest(event.sender_id))
    if (await check_user(event.sender_id)) == False:
        return await event.reply(f"{ok.user.first_name}, please join my channel to use me!", buttons=[Button.url("Join Channel", url="https://t.me/BotzHub")])
    try:
        await client.join_chat(invite_link)
        return "✅ **This channel is now supported, Now send me post link to get that post.**"
    except BadRequest:
        return "**Something Went wrong. I guess your link is invalid or expired or you have already Sent me link.**"
    except FloodWait:
        return "Flood wait error, Please report in Support Group."
    except Exception as e:
        return f"{str(e)}"
           
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
        
