import re
import yaml
from io import BytesIO

import requests
from PIL import Image
from ncatbot.core import BotClient, GroupMessage
from ncatbot.utils.config import config

from utils.findlink import decodeQR
from utils.wjxfiller import fillWJX


cfg = yaml.load(open('config.yaml', 'r', encoding="utf-8"), Loader=yaml.FullLoader).items()

config.set_bot_uin(cfg["qqid"])
config.set_ws_uri(cfg["ws_uri"])
config.set_token(cfg["token"])
bot = BotClient()
groups = {cfg["group_id"]}


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
