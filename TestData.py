from selenium.webdriver.common.by import By

BASE_URL = "https://devenv.investa.trade/login"
EMAIL = "thetestdummytest+tradebuyer@gmail.com"
PASSWORD = "123123"

class login:
    EMAIL = By.XPATH, "//input[@name='Username']"
    PASSWORD = By.XPATH, "//input[@name='Password']"
    SUBMIT = By.XPATH, "//button[@type='submit']"

class selectbroker:
    INVESTABROKER = By.XPATH, "//button[1]"
    BROKERTRADINGPIN =By.XPATH, "//input[@data-unique-tag='pinElementId4']"
    GO = By.XPATH, "//div[@class='btn ml-1 investa-btn-blue']"

class cashin:
    DEPOSIT = By.XPATH, "//a[@class='deposit-btn fs-14 px-2 py-1 d-flex align-items-center fw-700 mx-1']"
    AMOUNT = By.XPATH, "//input[@placeholder='0.00']"
    BPI = By.XPATH, "//label[@class='mb-0 normal-text regular dark-gray fs-14 c-point pr-2 ng-binding'][1]"
    CONTINUE = By.XPATH, "//button[normalize-space()='Continue']"
    METHOD = By.XPATH, "//p[@class='dark-gray fs-15 mb-0 ng-binding' and text()='BPI - Bank Deposit / Fund Transfer']"
    AMOUNTPAY= By.CSS_SELECTOR, "div[class='bg-light-gray br-10 d-flex justify-content-between flex-grow-1 p-3 flex-column'] div:nth-child(2) div:nth-child(1) div:nth-child(2) p:nth-child(1)"
    SUBMIT = By.XPATH, "//button[@type='button' and text()='Submit']"
    DEPOSITSLIP = By.XPATH, "//input[@name='depositSlip']"
    REFERENCENO = By.XPATH, "//input[@placeholder='Confirmation / Reference No.']"
    SUBMITPAYSLIP = By.XPATH, "//button[@class='investa-btn-blue']"
    DEPOSITNO = By.XPATH, "(//p[@class='mb-0 fs-13 white ng-binding'])[1]"
    DEPOSITNORESULT = By.CSS_SELECTOR, "body > div:nth-child(4) > div:nth-child(5) > div:nth-child(1) > div:nth-child(1) > div:nth-child(4) > div:nth-child(2) > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(2) > span:nth-child(1)"
    CASHIN=  By.XPATH, "//a[@href='/Wallet/AddFund']"