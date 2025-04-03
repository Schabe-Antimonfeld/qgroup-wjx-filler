import re

from selenium.webdriver import chrome
from selenium.webdriver.common.by import By


def get_questions(driver: chrome, n: int) -> list:
    """
    获取问卷题目\n
    :param driver: webdriver
    :param n: 题目数量
    :return: 问卷题目
    """
    typedict = {"1": "monoBlank", "3": "monoChoice"}
    choice = {"monoChoice"}
    questions = []
    for i in range(1, n + 1):
        q = driver.find_element(By.CSS_SELECTOR, f"#div{i}")
        tp = typedict[q.get_attribute("type")]
        text = tuple(q.text.lstrip("*").split("\n"))[1:]
        name = text[1]
        choices = text[2:] if tp in choice else None
        questions.append((tp, name, choices))
    return questions
