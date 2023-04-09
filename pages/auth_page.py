from settings import valid_email, valid_password
from .base_page import BasePage
from .locators import BaseLocators, AuthPageLocators, ChangePassPageLocators, RegistrationPageLocators, UserAgreementPageLocators


class AuthPage(BasePage):
    # AS001 метод проверки перехода на страницу форму авторизации
    def authorization_page_form_open(self):
        assert self.have_element(AuthPageLocators.AUTH_HEADING)
        assert "https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth" in self.driver.current_url, \
            "url do not match"

    # AS002 метод проверки перехода на страницу формы регистрации
    def open_registration_form_page(self):
        self.find_element(AuthPageLocators.AUTH_REGISTER_LINK).click()
        assert self.have_element(RegistrationPageLocators.REG_HEADING), "element not found"
        assert "https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/registration" \
               in self.driver.current_url, "url do not match"

    # AS003 метод проверки перехода на страницу формы восстановления пароля
    def open_password_recovery_form_page(self):
        self.find_element(AuthPageLocators.AUTH_FORGOT_PASSWORD_LINK).click()
        assert "https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/reset-credentials" \
               in self.driver.current_url, "url do not match"
        assert self.have_element(ChangePassPageLocators.CHANGE_PASS_HEADING), "element not found"

    # AS004 метод проверки перехода по ссылке авторизации с помощью Google.accaunt
    def link_authorization_from_google(self):
        self.find_element(AuthPageLocators.AUTH_SOCIAL_GOOGLE_LINK).click()
        assert "https://accounts.google.com/o/oauth2/auth/identifier" in self.driver.current_url, "url do not match"

    # AS005 метод проверки расположения меню выбора типа аутентификации
    def location_tab_menu(self):
        assert self.have_element(AuthPageLocators.AUTH_TAB_MENU), "element not found"

    # AS006 метод проверки расположения продуктового слогана и логотипа
    def location_slogan_and_logo(self):
        assert self.have_element(AuthPageLocators.AUTH_SLOGAN), "element not found"
        assert self.have_element(AuthPageLocators.AUTH_LOGO), "element not found"

    # AS007 метод проверки автоматического изменения выбора метода аутентификации
    def automatic_change_authentication(self):
        self.find_element(AuthPageLocators.AUTH_USERNAME_INPUT).send_keys(valid_email)
        self.find_element(BaseLocators.BODY).click()
        assert self.have_element(AuthPageLocators.AUTH_USERNAME_INPUT_ACTIV_EMAIL), "element not found"

    # AS008 метод проверки авторизации с несуществующим логином и поролем
    def authorization_with_invalid_email_and_password(self):
        self.find_element(AuthPageLocators.AUTH_USERNAME_INPUT).send_keys(valid_email)
        self.find_element(AuthPageLocators.AUTH_PASSWORD_INPUT).send_keys(valid_password)
        self.find_element(AuthPageLocators.AUTH_ENTER_BUTTON).click()
        assert self.have_element(AuthPageLocators.AUTH_ERROR_WRONG_LOGIN_OR_PASSWORD), "element not found"

    # AS009 метод проверки авторизации с незаполненными полями
    def authorization_with_blank_fields(self):
        self.find_element(AuthPageLocators.AUTH_TAB_PHONE).click()
        self.find_element(AuthPageLocators.AUTH_ENTER_BUTTON).click()
        assert self.have_element(AuthPageLocators.AUTH_ERROR_ENTER_PHONE_NUMBER), "element not found"
        assert "https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth" in self.driver.current_url, \
            "url do not match"

    # AS010 метод проверки перехода на страницу с пользовательским соглашением под кнопкой "Войти"
    def link_to_the_user_agreement_page(self):
        original_window = self.driver.current_window_handle
        assert len(self.driver.window_handles) == 1
        self.find_element(AuthPageLocators.AUTH_USER_AGREEMENT_LINK).click()
        for window_handle in self.driver.window_handles:
            if window_handle != original_window:
                self.driver.switch_to.window(window_handle)
            else:
                pass
        assert self.have_element(UserAgreementPageLocators.USER_AGREEMENT_HEADING), "element not found"
        assert "https://b2c.passport.rt.ru/sso-static/agreement/agreement.html" in self.driver.current_url, \
            "url do not match"

    # AS011 метод проверки перехода на страницу с пользовательским соглашением в футере страницы
    def link_fut_to_the_user_agreement_page(self):
        original_window = self.driver.current_window_handle
        assert len(self.driver.window_handles) == 1
        self.find_element(AuthPageLocators.AUTH_PRIVACY_POLICY_LINK).click()
        for window_handle in self.driver.window_handles:
            if window_handle != original_window:
                self.driver.switch_to.window(window_handle)
            else:
                pass
        assert self.have_element(UserAgreementPageLocators.USER_AGREEMENT_HEADING), "element not found"
        assert "https://b2c.passport.rt.ru/sso-static/agreement/agreement.html" in self.driver.current_url, \
            "url do not match"
