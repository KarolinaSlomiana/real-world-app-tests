from pages.base_page import BasePage


class CreateBankAccount(BasePage):
    def __init__(self, driver) -> None:
        super().__init__(driver)

    def is_at(self):
        return self.driver.current_url.endswith("/bankaccounts/new")

    def create_bank_account(self, bank_name, routing_number, account_number):
        driver = self.driver
        driver.find_element_by_id("bankaccount-bankName-input").send_keys(bank_name)
        driver.find_element_by_id("bankaccount - routingNumber - input").send_keys(routing_number)
        driver.find_element_by_id("bankaccount-accountNumber-input").send_keys(account_number)
        driver.find_element_by_css_selector("a.MuiButton-root:nth-child(1)").click()
        from pages.bank_accounts.bank_accounts import BankAccounts
        return BankAccounts(driver)