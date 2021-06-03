from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class SignUpPage(BasePage):

    # locators
    FIRST_NAME_INPUT = (By.ID, 'firstName')
    LAST_NAME_INPUT = (By.ID, 'lastName')
    USERNAME_INPUT = (By.ID, 'username')
    PASSWORD_INPUT = (By.ID, 'password')
    CONFIRM_PASSWORD_INPUT = (By.ID, 'confirmPassword')
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
        self.do_send_keys(self.FIRST_NAME_INPUT, first_name)
        self.do_send_keys(self.LAST_NAME_INPUT, last_name)
        self.do_send_keys(self.USERNAME_INPUT, username)
        self.do_send_keys(self.PASSWORD_INPUT, password)
        self.do_send_keys(self.CONFIRM_PASSWORD_INPUT, confirm_password)
        button_enabled = self.driver.find_elements_by_css_selector(".MuiButtonBase-root[tabindex='0']")
        if bool(button_enabled):
            self.do_click(self.SIGN_UP_BTN)

