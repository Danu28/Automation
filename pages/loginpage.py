from selenium.webdriver.common.by import By

from pages.basepage import BasePage
from pages.homepage import HomePage


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    username_field = (By.XPATH, "//input[@id='ctl00_mainContent_txtUserName']")
    password_field = (By.XPATH, "//input[@id='ctl00_mainContent_txtPassword']")
    signin_btn = (By.XPATH, "//input[@id='ctl00_mainContent_LoginButton']")
    signout_link = (By.XPATH, "//a[@href='../Signout.aspx']")
    invalid_user = (By.XPATH, "//span[normalize-space()='Invalid username/password']")

    def validate_user(self, username, password):
        status = False
        self.fill(self.username_field, username)
        self.fill(self.password_field, password)
        self.click(self.signin_btn)
        if self.is_displayed(self.signout_link):
            self.click(self.signout_link)
            status = True
        elif self.is_displayed(self.invalid_user):
            status = False
        return status


    def login_user(self, username, password):
        self.fill(self.username_field, username)
        self.fill(self.password_field, password)
        self.click(self.signin_btn)
        if self.is_displayed(self.signout_link):
            return HomePage(self.driver)
