from selenium.webdriver.common.by import By
from Pages import BasePage


class NewTransactionPage(BasePage):

    # locators
    SELECT_CONTACT_SEARCH_INPUT = (By.ID, 'user-list-search-input')