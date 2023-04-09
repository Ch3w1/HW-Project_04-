#python -m pytest -v --driver Chrome --driver-path F:/Selenium/chromedriver_win32/cromedriver.exe tests/test_registration_page.py

from pages.registration_page import RegPage
from settings import url_base_page, valid_email, valid_password, invalid_password, valid_password2

class TestRegistrationPage():
    def test_AS012_input_valid_email_or_phone_num(self, browser):
        reg_page = RegPage(browser, url_base_page)
        reg_page.open_page_registration()
        reg_page.input_valid_email_or_phone_num(valid_email)

    def test_AS013_input_invalid_pass_at_registration(self, browser):
        reg_page = RegPage(browser, url_base_page)
        reg_page.open_page_registration()
        reg_page.input_invalid_pass_at_registration(invalid_password)

    def test_AS014_input_valid_pass_at_registration(self, browser):
        reg_page = RegPage(browser, url_base_page)
        reg_page.open_page_registration()
        reg_page.input_valid_pass_at_registration(valid_password)

    def test_AS015_input_confirm_pass_at_registration(self, browser):
        reg_page = RegPage(browser, url_base_page)
        reg_page.open_page_registration()
        reg_page.input_confirm_pass_at_registration(valid_password, valid_password2)

    def test_AS018_link_to_the_user_agreement_page(self, browser):
        reg_page = RegPage(browser, url_base_page)
        reg_page.open_page_registration()
        reg_page.link_to_the_user_agreement_page()

    def test_AS019_link_fut_to_the_user_agreement_page(self, browser):
        reg_page = RegPage(browser, url_base_page)
        reg_page.open_page_registration()
        reg_page.link_fut_to_the_user_agreement_page()

    def test_AS021_location_logo_and_slogan_at_reg_page(self, browser):
        auth_page = RegPage(browser, url_base_page)
        auth_page.open_page()
        auth_page.location_logo_and_slogan_at_reg_page()
