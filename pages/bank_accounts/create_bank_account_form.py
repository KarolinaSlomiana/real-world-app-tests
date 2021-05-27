from pages.main_page import MainPage
from selenium.webdriver.common.by import By


class CreateBankAccount(MainPage):

    # locators
    BANK_ACC_NAME_INPUT = (By.ID, "bankaccount-bankName-input")
    BANK_ACC_ROUTING_NUM_INPUT = (By.ID, "bankaccount-routingNumber-input")
    BANK_ACC_NUM_INPUT = (By.ID, "bankaccount-accountNumber-input")
    SAVE_BANK_ACC_BTN = (By.CSS_SELECTOR, ".MuiButtonBase-root[type='submit']")

    def __init__(self, driver) -> None:
        super().__init__(driver)

    def is_at(self):
        return self.driver.current_url.endswith("/bankaccounts/new")

    def create_bank_account(self, bank_name, routing_number, account_number):
        driver = self.driver
        self.do_send_keys(self.BANK_ACC_NAME_INPUT, bank_name)
        self.do_send_keys(self.BANK_ACC_ROUTING_NUM_INPUT, routing_number)
        self.do_send_keys(self.BANK_ACC_NUM_INPUT, account_number)
        self.do_click(self.SAVE_BANK_ACC_BTN)
        from pages.bank_accounts.bank_accounts_tab import BankAccounts
        return BankAccounts(driver)
