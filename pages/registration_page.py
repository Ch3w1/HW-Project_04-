from .base_page import BasePage
from .locators import BaseLocators, RegistrationPageLocators, UserAgreementPageLocators


class RegPage(BasePage):
    # AS015 метод проверки ввода валидного e-mail или мобильного телефона
    def input_valid_email_or_phone_num(self, input_text):
        self.find_element(RegistrationPageLocators.REG_EMAIL_PHONE_INPUT).send_keys(input_text)
        self.find_element(BaseLocators.BODY).click()
        element = self.find_element(RegistrationPageLocators.REG_EMAIL_PHONE_INPUT_VALUE)
        value = element.get_attribute("value")
        assert input_text == value, "email or phone do not match"
        assert self.not_have_element(RegistrationPageLocators.REG_ERROR_INVALID_EMAIL_OR_PHONE_INPUT), "element found"

    # AS016 метод проверки ввода невалидного пароля при регистрации
    def input_invalid_pass_at_registration(self, input_text):
        self.find_element(RegistrationPageLocators.REG_PASSWORD_INPUT).send_keys(input_text)
        self.find_element(BaseLocators.BODY).click()
        assert self.have_element(RegistrationPageLocators.REG_ERROR_INVALID_PASSWORD_INPUT), "element not found"

    # AS017 метод проверки ввода валидного пароля при регистрации
    def input_valid_pass_at_registration(self, input_text):
        self.find_element(RegistrationPageLocators.REG_PASSWORD_INPUT).send_keys(input_text)
        self.find_element(BaseLocators.BODY).click()
        assert self.not_have_element(RegistrationPageLocators.REG_ERROR_INVALID_PASSWORD_INPUT), "element found"

    # AS018 метод проверки подтверждения пороля
    def input_confirm_pass_at_registration(self, password1, password2):
        self.find_element(RegistrationPageLocators.REG_PASSWORD_INPUT).send_keys(password1)
        self.find_element(RegistrationPageLocators.REG_PASSWORD_CONFIRM_INPUT).send_keys(password2)
        self.find_element(RegistrationPageLocators.REG_ENTER_BUTTON).click()
        assert self.have_element(RegistrationPageLocators.REG_ERROR_PASSWORD_DONT_MATCH), "element not found"

    # AS019 метод проверки перехода на страницу с пользовательским соглашением под кнопкой "Зарегестрироваться"
    def link_to_the_user_agreement_page(self):
        original_window = self.driver.current_window_handle
        assert len(self.driver.window_handles) == 1
        self.find_element(RegistrationPageLocators.REG_USER_AGREEMENT_LINK).click()
        for window_handle in self.driver.window_handles:
            if window_handle != original_window:
                self.driver.switch_to.window(window_handle)
            else:
                pass
        assert self.have_element(UserAgreementPageLocators.USER_AGREEMENT_HEADING), "element not found"
        assert "https://b2c.passport.rt.ru/sso-static/agreement/agreement.html" in self.driver.current_url, \
            "url do not match"

    # AS020 метод проверки перехода на страницу с пользовательским соглашением в футере страницы
    def link_fut_to_the_user_agreement_page(self):
        original_window = self.driver.current_window_handle
        assert len(self.driver.window_handles) == 1
        self.find_element(RegistrationPageLocators.REG_PRIVACY_POLICY_LINK).click()
        for window_handle in self.driver.window_handles:
            if window_handle != original_window:
                self.driver.switch_to.window(window_handle)
            else:
                pass
        assert self.have_element(UserAgreementPageLocators.USER_AGREEMENT_HEADING), "element not found"
        assert "https://b2c.passport.rt.ru/sso-static/agreement/agreement.html" in self.driver.current_url, \
            "url do not match"

    #AS021 метод проверки расположения логотипа и продуктового слогана на странице формы регистрации
    def location_logo_and_slogan_at_reg_page(self):
        assert self.have_element(RegistrationPageLocators.REG_LOGO), "element not found"
        assert self.have_element(RegistrationPageLocators.REG_SLOGAN), "element not found"