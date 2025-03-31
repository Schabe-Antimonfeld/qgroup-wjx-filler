import re
from io import BytesIO

import requests
from PIL import Image
from ncatbot.core import BotClient, GroupMessage
from ncatbot.utils.config import config

from utils.findlink import decodeQR
from utils.wjxfiller import fillWJX


config.set_bot_uin("2788278428")
config.set_ws_uri("ws://localhost:3001")
config.set_token("napcat")
bot = BotClient()
groups = {"1033143754"}


@bot.group_event()
async def on_group_message(msg: GroupMessage):
    pattern = r"https://www.wjx.cn/[a-zA-Z0-9/_\-]+.aspx"
    if msg.group_id in groups:
        if url := re.search(pattern, msg.raw_message):
            fillWJX(url.group())
    for segment in msg.message:
        if segment["type"] == "image":
            imgurl = segment["data"]["url"]
            response = requests.get(imgurl)
            image_data = BytesIO(response.content)
            img = Image.open(image_data)
            if url := decodeQR(img):
                fillWJX(url)


if __name__ == "__main__":
    bot.run()
