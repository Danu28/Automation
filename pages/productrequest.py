from selenium.webdriver.common.by import By

from pages.basepage import BasePage


class ProductRequest(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    partnerName = (By.XPATH, "//input[@id='partnerName']")
    email = (By.XPATH, "//input[@id='partnerEmail']")
    phone_no = (By.XPATH, "//input[@id='partnerPhone']")
    submit = (By.XPATH, "//button[@id='cmdsubmit']")

    def enter_data(self, name, email, ph_no):
        self.fill(self.partnerName, name)
        self.fill(self.email, email)
        self.fill(self.phone_no, ph_no)
        self.click(self.submit)
        return self.get_attribute_value(self.partnerName, "id")