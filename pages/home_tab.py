from pages.main_page import MainPage
from selenium.webdriver.common.by import By
from assets.data import TestData


class Home(MainPage):

    # locators
    WELCOME_INSCRIPTION = (By.CSS_SELECTOR, 'h2.MuiTypography-root.MuiTypography-h6')
    FILTER_BY_ASSOCIATION_EVERYONE_BTN = (By.CSS_SELECTOR, "a.MuiTab-root:nth-child(1)")
    FILTER_BY_ASSOCIATION_FRIENDS_BTN = (By.CSS_SELECTOR, "a.MuiTab-root:nth-child(2)")
    FILTER_BY_ASSOCIATION_MINE_BTN = (By.CSS_SELECTOR, "a.MuiTab-root:nth-child(3)")

    def __init__(self, driver) -> None:
        super().__init__(driver)

    def is_at(self):
        return self.driver.current_url == TestData.BASE_URL

    def filter_transactions(self, association, date, amount):
        if association == "everyone":
            self.do_click(self.FILTER_BY_ASSOCIATION_EVERYONE_BTN)
        if association == "friends":
            self.do_click(self.FILTER_BY_ASSOCIATION_FRIENDS_BTN)
        if association == "mine":
            self.do_click(self.FILTER_BY_ASSOCIATION_MINE_BTN)

        # to do: calendar and range slide
        self.driver.find_element_by_css_selector("div.MuiGrid-spacing-xs-1:nth-child(1) > div:nth-child(1) > "
                                                 "div:nth-child(1) > div:nth-child(1)").click()
        self.driver.find_element_by_css_selector(".Cal__Container__root").send_keys(date)
        self.driver.find_element_by_css_selector("div.MuiGrid-spacing-xs-1:nth-child(1) > div:nth-child(2) > "
                                                 "div:nth-child(1) > div:nth-child(1)")
        self.driver.find_element_by_css_selector(".makeStyles-amountRangeRoot-575").send_keys(amount)


