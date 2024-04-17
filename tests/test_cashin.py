import pytest

from pages.cashin_page import CashinPage
from tests.base_test import BaseTest

@pytest.mark.order(3)
class TestCashin(BaseTest):
    def test_cashin(self, driver):
        cashinpage = CashinPage(driver)
        cashinpage.gotodeposit()
        cashinpage.loop_cashin()