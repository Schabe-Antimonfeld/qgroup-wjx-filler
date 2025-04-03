import time

import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By

import utils.questiontype as qt
from utils.questionconfirm import get_questions


def fillWJX(url: str) -> None:
    """
    填写问卷星问卷\n
    请确保链接为问卷星问卷
    :param url: 问卷星问卷链接
    """
    option = webdriver.ChromeOptions()
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    option.add_experimental_option('useAutomationExtension', False)
    option.add_experimental_option("detach", True)
    service = webdriver.ChromeService(executable_path='chromedriver-win64/chromedriver.exe')
    driver = webdriver.Chrome(options=option, service=service)
    driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument',
                           {'source': 'Object.defineProperty(navigator, "webdriver", {get: () => undefined})'
                            })
    driver.set_window_size(600, 500)
    driver.set_window_position(x=400, y=50)
    driver.get(url)
    cfg = list(yaml.load(open('questionnaire.yaml', 'r', encoding="utf-8"), Loader=yaml.FullLoader).items())
    questions = get_questions(driver, len(cfg))
    for q in cfg:
        time.sleep(1.3)
        options = q[1]
        if options["type"] == "monoBlank":
            qt.monoBlank(driver, options["num"], options["ans"], options["random"])
        elif options["type"] == "monoChoice":
            qt.monoChoice(driver, options["num"], options["ans"], options["random"])
        elif options["type"] == "optional":
            if questions[q[1]["num"] - 1][0] == "monoBlank":
                qt.monoBlank(driver, options["num"], options["ans"], options["random"])
            elif questions[q[1]["num"] - 1][0] == "monoChoice":
                ans = []
                for choice in options["ans"]:
                    ans.append(questions[q[1]["num"] - 1][2].index(choice) + 1)
                try:
                    qt.monoChoice(driver, options["num"], ans, options["random"])
                except:
                    qt.monoChoice(driver, options["num"], [1], options["random"])
    driver.find_element(By.XPATH, '//*[@id="ctlNext"]').click()
