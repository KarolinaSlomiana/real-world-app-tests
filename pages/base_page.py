from abc import abstractmethod
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:

    """This is base class page for all Real World App pages"""

    def __init__(self, driver) -> None:
        """
        Initialize the page by passing driver instance

        :type driver: selenium.webdriver.remote.webdriver.WebDriver
        """
        self.driver = driver

    @abstractmethod
    def is_at(self):
        return False

    def do_click(self, by_locator):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator)).click()

    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self, by_locator):
        el = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator))
        return el.text
