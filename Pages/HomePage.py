import pytest
import selenium
from selenium.webdriver.common.by import By
from Pages import BasePage


class HomePage(BasePage):

    # locators
    SELECT_DATE_BTN = (By.CSS_SELECTOR, '.MuiGrid-spacing-xs-1 > div:nth-child(1) > div:nth-child(1) > '
                                        'div:nth-child(1)')
    #   DATA_CONTAINER
    SELECT_AMOUNT_BTN = (By.CSS_SELECTOR, '.MuiGrid-spacing-xs-1 > div:nth-child(2) > div:nth-child(1) >'
                                          ' div:nth-child(1)')
    AMOUNT_RANGE_SLIDER = (By.CSS_SELECTOR, '.makeStyles-amountRangeRoot-162')
    CREATE_TRANSACTION_BTN = (By.CSS_SELECTOR, 'a.MuiButton-root:nth-child(1)')

    # def filter_transactions(self, date, amount, association):
        # choose date
        # choose amount
        # choose association

