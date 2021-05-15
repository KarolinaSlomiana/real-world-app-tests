from selenium.webdriver.common.by import By
from Pages import BasePage


class MyAccountPage(BasePage):

    # locators
    FIRST_NAME_INPUT = (By.ID, 'user-settings-firstName-input')
    LAST_NAME_INPUT = (By.ID, 'user-settings-lastName-input')
    EMAIL_INPUT = (By.ID, 'user-settings-email-input')
    PHONE_NUMBER_INPUT = (By.ID, 'user-settings-phoneNumber-input')
    SAVE_BTN = (By.CSS_SELECTOR, 'button.MuiButton-root > span:nth-child(1)')

    # def change_data(self):
    # czy tu zrobić enuma, zeby przy wywoływaniu metody można było wybrać, które dane zmienić?
    # enum powinien mieć osobny plik?