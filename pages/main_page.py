from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):

    # locators
    SIDE_MENU_BTN = (By.CSS_SELECTOR, "button.MuiIconButton-root > span:nth-child(1)")
    HOME_BTN = (By.CSS_SELECTOR, "a.MuiListItem-root:nth-child(1)")
    MY_ACCOUNT_BTN = (By.CSS_SELECTOR, "a.MuiListItem-root:nth-child(2)")
    BANK_ACCOUNTS_BTN = (By.CSS_SELECTOR, "a.MuiListItem-root:nth-child(3)")
    NOTIFICATIONS_BTN = (By.CSS_SELECTOR, "a.MuiListItem-root:nth-child(4)")
    NOTIFICATIONS_BELL_BTN = (By.CSS_SELECTOR, "a.MuiIconButton-root > span:nth-child(1)")
    LOGOUT_BTN = (By.CSS_SELECTOR, "div.MuiListItem-root")
    NEW_TRANSACTION_BTN = (By.CSS_SELECTOR, ".MuiButton-label")

    def __init__(self, driver) -> None:
        super().__init__(driver)

    def is_at(self):
        return self.driver.current_url.endswith("/")

    def hide_side_menu(self):
        self.do_click(self.SIDE_MENU_BTN)

    def go_to_home_tab(self):
        self.do_click(self.HOME_BTN)
        from pages.home_tab import Home
        return Home(self.driver)

    def go_to_my_account_tab(self):
        self.do_click(self.MY_ACCOUNT_BTN)
        from pages.my_account_tab import MyAccount
        return MyAccount(self.driver)

    def go_to_bank_accounts_tab(self):
        self.do_click(self.BANK_ACCOUNTS_BTN)
        from pages.bank_accounts.bank_accounts_tab import BankAccounts
        return BankAccounts(self.driver)

    def go_to_notifications_tab(self):
        self.do_click(self.NOTIFICATIONS_BTN)
        from pages.notifications_tab import Notifications
        return Notifications(self.driver)

    def go_to_notifications_tab_by_bell(self):
        self.do_click(self.NOTIFICATIONS_BELL_BTN)
        from pages.notifications_tab import Notifications
        return Notifications(self.driver)

    def logout(self):
        self.do_click(self.LOGOUT_BTN)
        from pages.sign_in_page import SignInPage
        return SignInPage

    def go_to_new_transaction_tab(self):
        self.do_click(self.NEW_TRANSACTION_BTN)
        from pages.new_transaction_tab import NewTransaction
        return NewTransaction
