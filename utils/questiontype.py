from random import randint

from selenium.webdriver import chrome
from selenium.webdriver.common.by import By


def monoBlank(driver: chrome, num: int, ans: list, random: str) -> None:
    """
    单项填空\n
    只支持randint随机，其余均视为第一个答案
    :param driver: webdriver
    :param num: 题目编号
    :param ans: 备选答案
    :param random: 随机选项
    """
    if random == "randint":
        res = ans[randint(0, len(ans))]
    else:
        res = ans[0]
    driver.find_element(By.CSS_SELECTOR, f"#q{num}").send_keys(res)


def monoChoice(driver: chrome, num: int, ans: list, random: str) -> None:
    """
    单项选择\n
    只支持randint随机，其余均视为第一个答案
    :param driver: webdriver
    :param num: 题目编号
    :param ans: 备选答案
    :param random: 随机选项
    """
    if random == "randint":
        res = ans[randint(0, len(ans))]
    else:
        res = ans[0]
    driver.find_element(By.CSS_SELECTOR, f"#div{num} > div.ui-controlgroup > div:nth-child({res})").click()
