import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from configfiles.testdata import TestData
from utilities.utils import Utils


class BaseDriver:

    logger = Utils.get_logger()

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def wait_for_element(self, by_locator):
        element = self.wait.until(EC.presence_of_element_located(by_locator))
        return element

    def wait_for_all_elements(self, by_locator):
        elements = self.wait.until(EC.presence_of_all_elements_located(by_locator))
        return elements