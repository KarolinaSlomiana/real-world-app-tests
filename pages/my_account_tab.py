from pages.main_page import MainPage
from selenium.webdriver.common.by import By


class MyAccount(MainPage):

    # locators
    USER_STG_FIRST_NAME_INPUT = (By.ID, "user-settings-firstName-input")
    USER_STG_LAST_NAME_INPUT = (By.ID, "user-settings-lastName-input")
    USER_STG_EMAIL_INPUT = (By.ID, "user-settings-email-input")
    USER_STG_PHONE_NUM_INPUT = (By.ID, "user-settings-phoneNumber-input")
    USER_STG_SAVE_BTN = (By.CSS_SELECTOR, "button.MuiButton-root > span:nth-child(1)")

    def __init__(self, driver) -> None:
        super().__init__(driver)

    def is_at(self):
        return self.driver.current_url.endswith("/user/settings")

    def change_first_name(self, first_name):
        self.do_send_keys(self.USER_STG_FIRST_NAME_INPUT, first_name)
        self.do_click(self.USER_STG_SAVE_BTN)

    def change_last_name(self, last_name):
        self.do_send_keys(self.USER_STG_LAST_NAME_INPUT, last_name)
        self.do_click(self.USER_STG_SAVE_BTN)

    def change_email(self, email):
        self.do_send_keys(self.USER_STG_EMAIL_INPUT, email)
        self.do_click(self.USER_STG_SAVE_BTN)

    def change_phone_number(self, phone_number):
        self.do_send_keys(self.USER_STG_PHONE_NUM_INPUT, phone_number)
        self.do_click(self.USER_STG_SAVE_BTN)