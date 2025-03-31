import re

import pyzbar.pyzbar as pyzbar
from PIL import Image


def decodeQR(img: Image) -> str | None:
    """
    识别二维码并返回问卷星链接
    :param img: 二维码图片
    :return: 问卷星链接
    """
    decoded_objects = pyzbar.decode(img)
    if not decoded_objects:
        return None
    obj = decoded_objects[0]
    url = obj.data.decode('utf-8')
    pattern = r"https://www.wjx.cn/[a-zA-Z0-9/_\-]+.aspx"
    if re.match(pattern, url):
        return url
    return None
