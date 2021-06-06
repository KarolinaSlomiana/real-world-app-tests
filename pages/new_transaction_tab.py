from pages.main_layout import MainPage
from selenium.webdriver.common.by import By


class NewTransaction(MainPage):

    # locators
    SELECT_CONTACT_SEARCH_INPUT = (By.ID, 'user-list-search-input')
    FIRST_ITEM_IN_THE_CONTACT_LIST = (By.CSS_SELECTOR, "li.MuiListItem-root:nth-child(1)")
    TRANSACTION_AMOUNT_INPUT = (By.ID, "amount")
    TRANSACTION_NOTE_INPUT = (By.ID, "transaction-create-description-input")
    PAYMENT_REQUEST_BTN = (By.CSS_SELECTOR, 'button[data-test="transaction-create-submit-request"]')
    PAYMENT_BTN = (By.CSS_SELECTOR, 'button[data-test="transaction-create-submit-payment"]')

    def __init__(self, driver) -> None:
        super().__init__(driver)

    def is_at(self):
        return self.driver.current_url.endswith("/transaction/new")

    def choose_first_item_in_the_contact_list(self):
        self.do_click(self.FIRST_ITEM_IN_THE_CONTACT_LIST)

    def choose_nth_item_in_the_contact_list(self, n):
        NTH_ITEM_IN_THE_CONTACT_LIST = (By.CSS_SELECTOR, f"li.MuiListItem-root:nth-child({n})")
        self.do_click(NTH_ITEM_IN_THE_CONTACT_LIST)

    def choose_amount(self, amount):
        self.do_send_keys(self.TRANSACTION_AMOUNT_INPUT, amount)

    def write_note(self, note):
        self.do_send_keys(self.TRANSACTION_NOTE_INPUT, note)

    def submit_payment_request(self):
        self.do_click(self.PAYMENT_REQUEST_BTN)

    def submit_payment(self):
        self.do_click(self.PAYMENT_BTN)
