import random
import string
import time

import TestData
from pages.base_page import BasePage


class CashinPage(BasePage):
    def gotodeposit(self):
        time.sleep(1)
        assert self.url_is("https://devenv.investa.trade/Portfolio"), "invalid url"
        assert self.title_is("Portfolio | InvestaTrade"), "invalid title"

        self.wait_clickable(TestData.cashin.DEPOSIT).click()
    def cashin(self):

        time.sleep(2)

        assert self.url_is("https://devenv.investa.trade/Wallet/AddFund"), "invalid url"
        assert self.title_is("Cash In | InvestaTrade"), "invalid title"

        self.send_keys(TestData.cashin.AMOUNT, "100000")
        time.sleep(1)

        bpi = self.wait_visibility(TestData.cashin.BPI)
        self.action_click(bpi)
        time.sleep(0.5)

        continuebtn = self.wait_presence(TestData.cashin.CONTINUE)
        self.action_scroll_to_element(continuebtn)
        time.sleep(0.5)
        continuebtn.click()

        time.sleep(0.5)

        assert self.get_text(TestData.cashin.METHOD) == "BPI - Bank Deposit / Fund Transfer"
        assert self.get_text(TestData.cashin.AMOUNTPAY) == "PHP 100,000"

        self.wait_clickable(TestData.cashin.SUBMIT).click()
        time.sleep(1.5)

        submitbtn = self.wait_presence(TestData.cashin.SUBMITPAYSLIP)
        self.action_scroll_to_element(submitbtn)

        path = r"C:\Users\Leonard\Downloads\example image.png"
        self.file_upload(TestData.cashin.DEPOSITSLIP, path)

        referencevalue = ''.join(random.choices(string.digits, k=7))

        self.send_keys(TestData.cashin.REFERENCENO, referencevalue)
        time.sleep(1)

        text = self.get_text(TestData.cashin.DEPOSITNO)

        depositno = text[len("Deposit No. "):]

        submitpayslip = self.wait_presence(TestData.cashin.SUBMITPAYSLIP)
        self.action_click(submitpayslip)

        time.sleep(1)

        refno = self.get_text(TestData.cashin.DEPOSITNORESULT)

        assert refno == depositno, f"wrong {refno} and {depositno}"

        time.sleep(1)
        self.wait_clickable(TestData.cashin.CASHIN).click()
        cashin = self.wait_clickable(TestData.cashin.CASHIN)
        try:

            self.action_click(cashin)
        except Exception as e:
            print(e)


    def loop_cashin(self):
        for _ in range(50):
            self.cashin()




