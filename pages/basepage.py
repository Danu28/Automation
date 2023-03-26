import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

import configfiles.testdata
from base.base_driver import BaseDriver
from utilities.utils import Utils

""" This class is the parent class of all pages"""
""" This will contain all the generic methods"""


class BasePage(BaseDriver):

    logger = Utils.get_logger()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)

    def click(self, by_locator):
        self.wait_for_element(by_locator).click()

    def fill(self, by_locator, text):
        self.wait_for_element(by_locator).send_keys(text)

    def right_click(self, by_locator):
        element = self.wait_for_element(by_locator)
        action = ActionChains(self.driver)
        action.context_click(element).perform()

    def double_click(self, by_locator):
        element = self.wait_for_element(by_locator)
        action = ActionChains(self.driver)
        action.double_click(element).perform()

    def hover(self, by_locator):
        element = self.wait_for_element(by_locator)
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()

    def get_text(self, by_locator):
        element = self.wait_for_element(by_locator)
        return element.text

    def select_by_text(self, by_locator, text):
        element = self.wait_for_element(by_locator)
        select = Select(element)
        select.select_by_visible_text(text)

    def select_by_index(self, by_locator, index):
        element = self.wait_for_element(by_locator)
        select = Select(element)
        select.select_by_index(index)

    def select_by_value(self, by_locator, value):
        element = self.wait_for_element(by_locator)
        select = Select(element)
        select.select_by_value(value)

    def get_attribute_value(self, by_locator, attribute_type):
        return self.wait_for_element(by_locator).get_attribute(attribute_type)

    def close_window(self):
        self.driver.close()

    def close_browser(self):
        self.driver.quit()