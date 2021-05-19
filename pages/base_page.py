from abc import abstractmethod


class BasePage:
    def __init__(self, driver) -> None:
        """
        Initialize the page by passing driver instance

        :type driver: selenium.webdriver.remote.webdriver.WebDriver
        """
        self.driver = driver

    @abstractmethod
    def is_at(self):
        return False

    def hide_side_menu(self):
        side_menu_btn = self.driver.find_element_by_css_selector("button.MuiIconButton-root > span:nth-child(1)")
        side_menu_btn.click()

    def go_to_home_tab(self):
        self.driver.find_element_by_css_selector("a.MuiListItem-root:nth-child(1)").click()
        from pages.home_page import HomePage
        return HomePage(self.driver)

    def go_to_my_account_tab(self):
        self.driver.find_element_by_css_selector("a.MuiListItem-root:nth-child(2)").click()
        from pages.my_account import MyAccount
        return MyAccount(self.driver)

    def go_to_bank_accounts_tab(self):
        self.driver.find_element_by_css_selector("a.MuiListItem-root:nth-child(3)").click()
        from pages.bank_accounts.bank_accounts import BankAccounts
        return BankAccounts(self.driver)

    def go_to_notifications_tab(self):
        self.driver.find_element_by_css_selector("a.MuiListItem-root:nth-child(4)").click()
        from pages.notifications import Notifications
        return Notifications(self.driver)

    def go_to_notifications_tab_by_bell(self):
        self.driver.find_element_by_css_selector("a.MuiIconButton-root > span:nth-child(1)").click()
        from pages.notifications import Notifications
        return Notifications(self.driver)

    def logout(self):
        self.driver.find_element_by_css_selector("div.MuiListItem-root").click()
        from pages.login_page import LoginPage
        return LoginPage

    def go_to_new_transaction_tab(self):
        self.driver.find_element_by_css_selector(".MuiButton-root").click()
        from pages.new_transaction import NewTransaction
        return NewTransaction
