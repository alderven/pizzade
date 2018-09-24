import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import selenium.common.exceptions as exceptions


TIMEOUT = 30
DELIMITER = ','


def main(driver, ec, config):
    locator_type, locator = config.split(DELIMITER)
    locator_type = eval('By.' + locator_type)
    element = WebDriverWait(driver, TIMEOUT).until(ec((locator_type, locator)))
    allure.attach(driver.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
    return element


def find_element(driver, config):
    element = main(driver, EC.presence_of_element_located, config)
    return element


def enter_text(driver, config, text):
    element = find_element(driver, config)
    element.clear()
    element.send_keys(text)


def click(driver, config):
    element = find_element(driver, config)
    try:
        element.click()
    except exceptions.WebDriverException:
        driver.execute_script("arguments[0].click();", element)


def element_exists(driver, config):
    try:
        find_element(driver, config)
    except exceptions.NoSuchElementException:
        return False
    except exceptions.TimeoutException:
        return False
    return True
