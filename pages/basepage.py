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
        try:
            self.driver.get(url)
        except:
            self.logger.error(url + " open url failed ")

    def click(self, by_locator):
        try:
            self.wait_for_element(by_locator).click()
        except:
            self.logger.error(str(by_locator)+" click failed ")

    def fill(self, by_locator, text):
        try:
            element = self.wait_for_element(by_locator)
            element.clear()
            element.send_keys(text)
        except:
            self.logger.error(str(by_locator)+" fill failed ")

    def right_click(self, by_locator):
        try:
            element = self.wait_for_element(by_locator)
            action = ActionChains(self.driver)
            action.context_click(element).perform()
        except:
            self.logger.error(str(by_locator) + " right_click failed ")


    def double_click(self, by_locator):
        try:
            element = self.wait_for_element(by_locator)
            action = ActionChains(self.driver)
            action.double_click(element).perform()
        except:
            self.logger.error(str(by_locator) + " double_click failed ")

    def hover(self, by_locator):
        try:
            element = self.wait_for_element(by_locator)
            action = ActionChains(self.driver)
            action.move_to_element(element).perform()
        except:
            self.logger.error(str(by_locator) + " hover failed ")

    def get_text(self, by_locator):
        try:
            element = self.wait_for_element(by_locator)
            return element.text
        except:
            self.logger.error(str(by_locator) + " get_text failed ")

    def select_by_text(self, by_locator, text):
        try:
            element = self.wait_for_element(by_locator)
            select = Select(element)
            select.select_by_visible_text(text)
        except:
            self.logger.error(str(by_locator) + " select_by_text failed ")

    def select_by_index(self, by_locator, index):
        try:
            element = self.wait_for_element(by_locator)
            select = Select(element)
            select.select_by_index(index)
        except:
            self.logger.error(str(by_locator) + " select_by_index failed ")

    def select_by_value(self, by_locator, value):
        try:
            element = self.wait_for_element(by_locator)
            select = Select(element)
            select.select_by_value(value)
        except:
            self.logger.error(str(by_locator) + " select_by_value failed ")

    def get_attribute_value(self, by_locator, attribute_type):
        try:
            return self.wait_for_element(by_locator).get_attribute(attribute_type)
        except:
            self.logger.error(str(by_locator) + " get_attribute_value failed ")

    def close_window(self):
        try:
            self.driver.close()
        except:
            self.logger.error(" close_window failed ")

    def close_browser(self):
        try:
            self.driver.quit()
        except:
            self.logger.error(" close_browser failed ")
