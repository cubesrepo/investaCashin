import time

import TestData
from pages.base_page import BasePage


class BrokerPage(BasePage):
    def selectbroker(self):
        time.sleep(1)

        assert self.url_is("https://devenv.investa.trade/Welcome/Onboarding/BrokerSelection"), "invalid url"

        self.wait_visibility(TestData.selectbroker.INVESTABROKER).click()
        time.sleep(0.5)

        self.send_keys(TestData.selectbroker.BROKERTRADINGPIN, TestData.PASSWORD)
        time.sleep(0.5)

        self.wait_clickable(TestData.selectbroker.GO).click()

