from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class SignUpPage(BasePage):

    # locators
    FIRST_NAME = (By.ID, 'firstName')
    LAST_NAME = (By.ID, 'lastName')
    USERNAME = (By.ID, 'username')
    PASSWORD = (By.ID, 'password')
    CONFIRM_PASSWORD = (By.ID, 'confirmPassword')
    SIGN_UP_BTN = (By.CSS_SELECTOR, ".MuiButtonBase-root[tabindex='0']")
    SIGN_IN_LINK = (By.CSS_SELECTOR, '.MuiGrid-root > a')
    PASSWORD_HELPER_TEXT = (By.ID, 'password-helper-text')
    CONFIRM_PASSWORD_HELPER_TEXT = (By.ID, 'confirmPassword-helper-text')

    def __init__(self, driver) -> None:
        super().__init__(driver)

    def is_at(self):
        return self.driver.current_url.endswith("/signup")

    def go_to_sign_in_page(self):
        self.do_click(self.SIGN_IN_LINK)
        self.do_click(self.SIGN_IN_LINK)

    def do_sign_up(self, first_name, last_name, username, password, confirm_password):
        self.do_send_keys(self.FIRST_NAME, first_name)
        self.do_send_keys(self.LAST_NAME, last_name)
        self.do_send_keys(self.USERNAME, username)
        self.do_send_keys(self.PASSWORD, password)
        self.do_send_keys(self.CONFIRM_PASSWORD, confirm_password)
        button_enabled = self.driver.find_elements_by_css_selector(".MuiButtonBase-root[tabindex='0']")
        if bool(button_enabled):
            self.do_click(self.SIGN_UP_BTN)

    def get_different_password_confirmation_text(self):
        text = self.get_element_text(self.CONFIRM_PASSWORD_HELPER_TEXT)
        return text

    def get_incorrect_password_text(self):
        text = self.get_element_text(self.PASSWORD_HELPER_TEXT)
        return text
