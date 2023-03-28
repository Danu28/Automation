from selenium.webdriver.common.by import By

from pages.basepage import BasePage


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    signout_link = (By.XPATH, "//a[@href='../Signout.aspx']")



