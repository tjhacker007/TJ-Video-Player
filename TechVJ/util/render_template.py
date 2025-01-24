import jinja2
import logging
import aiohttp
from info import *
import urllib.parse
from TechVJ.bot import TechVJBot, TechVJBackUpBot
from TechVJ.util.human_readable import humanbytes
from TechVJ.server.exceptions import InvalidHash
from pyrogram.errors import FloodWait
from TechVJ.util.file_properties import get_name, get_hash, get_media_file_size, get_file_ids

async def render_page(id, user, src=None):
    try:
        file = await TechVJBot.get_messages(int(LOG_CHANNEL), int(id))
    except:
        file = await TechVJBackUpBot.get_messages(int(LOG_CHANNEL), int(id))
    file_data = await get_file_ids(file)
    src = urllib.parse.urljoin(
        STREAM_URL + "dl/",
        f"{id}/{urllib.parse.quote_plus(file_data.file_name)}?hash={file_data.unique_id[:6]}",
    )
    tag = file_data.mime_type.split("/")[0].strip()
    file_size = humanbytes(file_data.file_size)
    if tag in ["video", "audio"]:
        template_file = "TechVJ/template/req.html"
    else:
        template_file = "TechVJ/template/dl.html"
        async with aiohttp.ClientSession() as s:
            async with s.get(src) as u:
                file_size = humanbytes(int(u.headers.get("Content-Length")))

    with open(template_file) as f:
        template = jinja2.Template(f.read())

    file_name = file_data.file_name.replace("_", " ")

    return template.render(
        file_name=file_name,
        file_url=src,
        file_size=file_size,
        user_id=user
    )
