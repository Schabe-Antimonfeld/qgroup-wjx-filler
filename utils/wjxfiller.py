import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By

import utils.questiontype as qt


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
    cfg = list(yaml.load(open('config.yaml', 'r', encoding="utf-8"), Loader=yaml.FullLoader).items())
    for q in cfg:
        if q[1]["type"] == "monoBlank":
            qt.monoBlank(driver, q)
        elif q[1]["type"] == "monoChoice":
            qt.monoChoice(driver, q)
    driver.find_element(By.XPATH, '//*[@id="ctlNext"]').click()
