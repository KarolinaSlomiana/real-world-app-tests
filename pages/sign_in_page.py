from selenium.webdriver.common.by import By
from pages.home_tab import Home
from pages.base_page import BasePage
from pages.sign_up_page import SignUpPage
from pages.main_layout import MainPage


class SignInPage(BasePage):

    # locators
    USER_NAME = (By.ID, 'username')
    PASSWORD = (By.ID, 'password')
    LOGIN_BTN = (By.CSS_SELECTOR, "button.MuiButtonBase-root[tabindex='0']")
    SIGN_UP_LINK = (By.CSS_SELECTOR, 'a[href="/signup"]')
    INCORRECT_CREDENTIALS_MESSAGE = (By.CSS_SELECTOR, ".MuiAlert-message")

    def __init__(self, driver) -> None:
        super().__init__(driver)

    def is_at(self):
        return self.driver.current_url.endswith("/signin")

    def go_to_sign_up_page(self):
        self.do_click(self.SIGN_UP_LINK)
        self.do_click(self.SIGN_UP_LINK)
        return SignUpPage(self.driver)

    def do_login(self, username, password):
        self.do_send_keys(self.USER_NAME, username)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.LOGIN_BTN)
        # if username == 'Katharina_Bernier':
        #    return MainPage(self.driver)
        return Home(self.driver)

    def get_incorrect_credentials_text(self):
        text = self.get_element_text(self.INCORRECT_CREDENTIALS_MESSAGE)
        return text
