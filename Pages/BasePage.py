from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


class BasePage:

    # locators
    HOME_BTN = (By.CSS_SELECTOR, 'a.MuiListItem-root:nth-child(1)')
    MY_ACCOUNT_BTN = (By.CSS_SELECTOR, 'a.MuiListItem-root:nth-child(2)')
    BANK_ACCOUNTS_BTN = (By.CSS_SELECTOR, 'a.MuiListItem-root:nth-child(3)')
    NOTIFICATIONS_BTN = (By.CSS_SELECTOR, 'a.MuiListItem-root:nth-child(4)')
    LOGOUT_BTN = (By.CSS_SELECTOR, 'div.MuiListItem-root')
    HIDE_SIDE_MENU_BTN = (By.CSS_SELECTOR, 'button.MuiIconButton-root > span:nth-child(1)')
    NEW_TRANSACTION_BTN = (By.CSS_SELECTOR, '.MuiButton-root')
    NOTIFICATIONS_BELL_BTN = (By.CSS_SELECTOR, 'a.MuiIconButton-root > span:nth-child(1)')

    def __init__(self, driver):
        self.driver = driver

    def do_click(self, by_locator):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator)).click()

    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self, by_locator):
        el = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator))
        return el.text

    def is_visible(self, by_locator):
        el = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator))
        return bool(el)

    def hide_side_menu(self):
        self.do_click(self.HIDE_SIDE_MENU_BTN)
