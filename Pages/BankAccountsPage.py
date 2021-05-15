from selenium.webdriver.common.by import By
from Pages import BasePage
import database


class BankAccountsPage(BasePage):

    CREATE_BANK_ACCOUNT_BTN = (By.CSS_SELECTOR, 'a.MuiButton-root:nth-child(1)')
    BANK_NAME_INPUT = (By.ID, 'bankaccount-bankName-input')
    ROUTING_NUMBER_INPUT = (By.ID, 'bankaccount - routingNumber - input')
    ACCOUNT_NUMBER_INPUT = (By.ID, 'bankaccount-accountNumber-input')
    SAVE_CREATED_ACCOUNT_BTN = (By.CSS_SELECTOR, 'button.MuiButton-root')

    def create_bank_account(self):
        self.do_click(self.CREATE_BANK_ACCOUNT_BTN)
        self.do_send_keys(self.BANK_NAME_INPUT, database.TestData.BANK_NAME)
        self.do_send_keys(self.ROUTING_NUMBER_INPUT, database.TestData.ROUTING_NUMBER)
        self.do_send_keys(self.ACCOUNT_NUMBER_INPUT, database.TestData.ACCOUNT_NUMBER)
        self.do_click(self.SAVE_CREATED_ACCOUNT_BTN)
