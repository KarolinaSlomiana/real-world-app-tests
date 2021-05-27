from pages.main_page import MainPage
from selenium.webdriver.common.by import By


class BankAccounts(MainPage):

    # locators
    CREATE_BANK_ACCOUNT_BTN = (By.CSS_SELECTOR, "a.MuiButton-root:nth-child(1)")
    DELETE_BANK_ACCOUNT_BTN = (By.CSS_SELECTOR, ".MuiGrid-align-items-xs-flex-start > div:nth-child(2)")

    def __init__(self, driver) -> None:
        super().__init__(driver)

    def is_at(self):
        return self.driver.current_url.endswith("/bankaccounts")

    def open_create_bank_account_form(self):
        self.do_click(self.CREATE_BANK_ACCOUNT_BTN)
        from pages.bank_accounts.create_bank_account_form import CreateBankAccount
        return CreateBankAccount(self.driver)

    def delete_bank_account(self):
        self.do_click(self.DELETE_BANK_ACCOUNT_BTN)


