import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    print("\n start browser for test..")
    browser = webdriver.Chrome()
    browser.maximize_window()
    yield browser
    print("\n quit browser..")
    browser.quit()