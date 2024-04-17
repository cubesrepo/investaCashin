import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeChromiumService
from selenium.webdriver.firefox.service import Service as GeckoDriverService
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.chrome import ChromeDriverManager

import TestData


@pytest.fixture(scope="session")
def driver(request):
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
    elif browser == "firefox":
        service = GeckoDriverService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)
    elif browser == "edge":
        service = EdgeChromiumService(EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(service=service)
    else:
        raise ValueError(f"unsupported browser {browser}")
    driver.maximize_window()
    driver.get(TestData.BASE_URL)
    yield driver
    time.sleep(3)
    driver.quit()

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")