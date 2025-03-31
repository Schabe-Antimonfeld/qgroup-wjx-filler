from random import randint

from selenium.webdriver import chrome
from selenium.webdriver.common.by import By


def monoBlank(driver: chrome, q: dict) -> None:
    """
    单项填空\n
    只支持randint随机，其余均视为第一个答案
    :param driver: webdriver
    :param q: 题目信息
    """
    if q[1]["random"] == "randint":
        lst = q[1]["ans"]
        ans = lst[randint(0, len(lst))]
    else:
        ans = q[1]["ans"][0]
    driver.find_element(By.CSS_SELECTOR, f"#q{q[1]["num"]}").send_keys(ans)


def monoChoice(driver: chrome, q: dict) -> None:
    """
    单项选择\n
    只支持randint随机，其余均视为第一个答案
    :param driver: webdriver
    :param q: 题目信息
    """
    if q[1]["random"] == "randint":
        lst = q[1]["ans"]
        ans = lst[randint(0, len(lst))]
    else:
        ans = q[1]["ans"][0]
    driver.find_element(By.CSS_SELECTOR, f"#div{q[1]["num"]} > div.ui-controlgroup > div:nth-child({ans})").click()
