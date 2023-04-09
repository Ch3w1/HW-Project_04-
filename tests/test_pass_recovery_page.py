#python -m pytest -v --driver Chrome --driver-path F:/Selenium/chromedriver_win32/cromedriver.exe  tests/test_pass_recovery_page.py

from pages.pass_recovery_page import PassRecoveryPage
from settings import url_pass_recovery

class TestPassRecoveryPage():
    def test_AS012_password_recovery_with_blank_fields(self, browser):
        change_pass_page = PassRecoveryPage(browser, url_pass_recovery)
        change_pass_page.open_page()
        change_pass_page.password_recovery_with_blank_fields()

    def test_AS013_password_recovery_with_blank_captcha(self, browser):
        change_pass_page = PassRecoveryPage(browser, url_pass_recovery)
        change_pass_page.open_page()
        change_pass_page.password_recovery_with_blank_fields()

    def test_AS014_link_fut_to_the_user_agreement_page(self, browser):
        change_pass_page = PassRecoveryPage(browser, url_pass_recovery)
        change_pass_page.open_page()
        change_pass_page.link_to_the_user_agreement_page()
