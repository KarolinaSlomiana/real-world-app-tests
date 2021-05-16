from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage
from Pages.SignupPage import SignupPage
from Pages.HomePage import HomePage
import database


class LoginPage(BasePage):

    USER_NAME = (By.ID, 'username')
    PASSWORD = (By.ID, 'password')
    LOGIN_BTN = (By.CSS_SELECTOR, "button.MuiButtonBase-root[tabindex='0']")
    SIGN_UP_LINK = (By.CSS_SELECTOR, ".MuiGrid-item > a")
    INCORRECT_CREDENTIALS_MESSAGE = (By.CSS_SELECTOR, ".MuiAlert-message")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(database.TestData.BASE_URL)

    def do_login(self):
        self.do_send_keys(self.USER_NAME, database.TestData.username)
        self.do_send_keys(self.PASSWORD, database.TestData.password)
        self.do_click(self.LOGIN_BTN)
        return HomePage(self.driver)

    def go_to_signup_page(self):
        self.do_click(self.SIGN_UP_LINK)
        self.do_click(self.SIGN_UP_LINK)
        return SignupPage(self.driver)
