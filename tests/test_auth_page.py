#python -m pytest -v --driver Chrome --driver-path F:/Selenium/chromedriver_win32/cromedriver.exe  tests/test_auth_page.py

from pages.auth_page import AuthPage
from settings import url_base_page

class TestAuthPage():
    def test_AS001_authorization_page_form_open(self, browser):
        auth_page = AuthPage(browser, url_base_page)
        auth_page.open_page()
        auth_page.authorization_page_form_open()

    def test_AS002_open_registration_form_page(self, browser):
        auth_page = AuthPage(browser, url_base_page)
        auth_page.open_page()
        auth_page.open_registration_form_page()

    def test_AS003_open_password_recovery_form_page(self, browser):
        auth_page = AuthPage(browser, url_base_page)
        auth_page.open_page()
        auth_page.open_password_recovery_form_page()

    def test_AS004_link_authorization_from_google(self, browser):
        auth_page = AuthPage(browser, url_base_page)
        auth_page.open_page()
        auth_page.link_authorization_from_google()

    def test_AS005_location_tab_menu(self, browser):
        auth_page = AuthPage(browser, url_base_page)
        auth_page.open_page()
        auth_page.location_tab_menu()

    def test_AS006_location_slogan_and_logo(self, browser):
        auth_page = AuthPage(browser, url_base_page)
        auth_page.open_page()
        auth_page.location_slogan_and_logo()

    def test_AS007_automatic_change_authentication(self, browser):
        auth_page = AuthPage(browser, url_base_page)
        auth_page.open_page()
        auth_page.automatic_change_authentication()

    def test_AS008_authorization_with_invalid_email_and_password(self, browser):
        auth_page = AuthPage(browser, url_base_page)
        auth_page.open_page()
        auth_page.authorization_with_invalid_email_and_password()

    def test_AS009_authorization_with_blank_fields(self, browser):
        auth_page = AuthPage(browser, url_base_page)
        auth_page.open_page()
        auth_page.authorization_with_blank_fields()

    def test_AS010_link_to_the_user_agreement_page(self, browser):
        auth_page = AuthPage(browser, url_base_page)
        auth_page.open_page()
        auth_page.link_to_the_user_agreement_page()

    def test_AS011_link_fut_to_the_user_agreement_page(self, browser):
        auth_page = AuthPage(browser, url_base_page)
        auth_page.open_page()
        auth_page.link_fut_to_the_user_agreement_page()