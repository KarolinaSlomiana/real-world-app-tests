from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage


class SignupPage(BasePage):

    FIRST_NAME = (By.ID, 'firstName')
    LAST_NAME = (By.ID, 'lastName')
    USERNAME = (By.ID, 'username')
    PASSWORD = (By.ID, 'password')
    CONFIRM_PASSWORD = (By.ID, 'confirmPassword')
    SIGN_UP_BTN = (By.CSS_SELECTOR, ".MuiButtonBase-root[tabindex='0']")
    SIGN_IN_LINK = (By.CSS_SELECTOR, '.MuiGrid-root > a')
    PASSWORD_HELPER_TEXT = (By.ID, 'password-helper-text')
    CONFIRM_PASSWORD_HELPER_TEXT = (By.ID, 'confirmPassword-helper-text')

    def __init__(self, driver):
        super().__init__(driver)