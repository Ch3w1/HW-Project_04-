from settings import valid_email
from .base_page import BasePage
from .locators import ChangePassPageLocators, UserAgreementPageLocators


class PassRecoveryPage(BasePage):
    # AS012 метод проверки восстановления пароля с незаполненными полями
    def password_recovery_with_blank_fields(self):
        self.find_element(ChangePassPageLocators.CHANGE_PASS_TAB_PHONE).click()
        self.find_element(ChangePassPageLocators.CHANGE_PASS_CONTINUE_BUTTON).click()
        assert "https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/reset-credentials" \
               in self.driver.current_url, "url do not match"
        assert self.have_element(ChangePassPageLocators.CHANGE_PASS_ERROR_ENTER_PHONE_NUMBER), \
            "element not found"

    # AS013 метод проверки восстановления пароля с незаполненным полем капчи
    def password_recovery_with_blank_captcha(self):
        self.find_element(ChangePassPageLocators.CHANGE_PASS_TAB_MAIL).click()
        self.find_element(ChangePassPageLocators.CHANGE_PASS_USERNAME_INPUT).send_keys(valid_email())
        self.find_element(ChangePassPageLocators.CHANGE_PASS_CONTINUE_BUTTON).click()
        assert "https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/reset-credentials" \
               in self.driver.current_url, "url do not match"
        assert self.have_element(ChangePassPageLocators.CHANGE_PASS_ERROR_INVALID_USERNAME_OR_TEXT), \
            "element not found"

    #AS014 метод проверки перехода на страницу с пользовательским соглашением в футере формы восстановления пароля
    def link_to_the_user_agreement_page(self):
        original_window = self.driver.current_window_handle
        assert len(self.driver.window_handles) == 1
        self.find_element(ChangePassPageLocators.CHANGE_PASS_PRIVACY_POLICY_LINK).click()
        for window_handle in self.driver.window_handles:
            if window_handle != original_window:
                self.driver.switch_to.window(window_handle)
            else:
                pass
        assert self.have_element(UserAgreementPageLocators.USER_AGREEMENT_HEADING), "element not found"
        assert "https://b2c.passport.rt.ru/sso-static/agreement/agreement.html" in self.driver.current_url, \
            "url do not match"