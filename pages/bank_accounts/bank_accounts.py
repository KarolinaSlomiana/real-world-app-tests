from pages.base_page import BasePage


class BankAccounts(BasePage):
    def __init__(self, driver) -> None:
        super().__init__(driver)

    def is_at(self):
        return self.driver.current_url.endswith("/bankaccounts")

    def open_create_bank_account_form(self):
        create_bank_account_btn = self.driver.find_element_by_css_selector("a.MuiButton-root:nth-child(1)")
        create_bank_account_btn.click()
        from pages.bank_accounts.create_bank_account_form import CreateBankAccount
        return CreateBankAccount(self.driver)

    def delete_bank_account(self):
        delete_bank_account_btn = self.driver.find_element_by_css_selector(".MuiGrid-align-items-xs-flex-start > "
                                                                           "div:nth-child(2)")
        delete_bank_account_btn.click()


