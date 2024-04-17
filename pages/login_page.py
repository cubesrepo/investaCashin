import time

import TestData
from pages.base_page import BasePage


class LoginPage(BasePage):
    def login(self):

        self.send_keys(TestData.login.EMAIL, TestData.EMAIL)
        time.sleep(0.5)

        self.send_keys(TestData.login.PASSWORD, TestData.PASSWORD)
        time.sleep(0.5)

        self.wait_clickable(TestData.login.SUBMIT).click()


