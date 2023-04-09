from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchFrameException, TimeoutException
from .locators import AuthPageLocators

class BasePage(object):
    def __init__(self, driver, url, timeout=10):
        self.url = url
        self.driver = driver
        self.driver.implicitly_wait(timeout)

    def open_page(self):
        self.driver.get(self.url)

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator), message=f"Не удается найти элемент по локатору {locator}")

    def open_page_registration(self):
        self.driver.get(self.url)
        self.find_element(AuthPageLocators.AUTH_REGISTER_LINK).click()

    def have_element(self, what):
        try:
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((what)))
        except (NoSuchFrameException):
            return False
        return True

    def not_have_element(self, what):
        try:
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(what))
        except (TimeoutException):
            return True
        return False
