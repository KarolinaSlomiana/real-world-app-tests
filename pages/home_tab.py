from pages.main_layout import MainPage
from selenium.webdriver.common.by import By
from tests.test_home_page.data import HomePageData


class Home(MainPage):

    # locators
    WELCOME_INSCRIPTION = (By.CSS_SELECTOR, 'h2.MuiTypography-root.MuiTypography-h6')
    FILTER_BY_ASSOCIATION_EVERYONE_BTN = (By.CSS_SELECTOR, "a.MuiTab-root:nth-child(1)")
    FILTER_BY_ASSOCIATION_FRIENDS_BTN = (By.CSS_SELECTOR, "a.MuiTab-root:nth-child(2)")
    FILTER_BY_ASSOCIATION_MINE_BTN = (By.CSS_SELECTOR, "a.MuiTab-root:nth-child(3)")
    CHOSEN_ASSOCIATION_TEXT_DIV = (By.CSS_SELECTOR, ".MuiListSubheader-root")

    def __init__(self, driver) -> None:
        super().__init__(driver)

    def is_at(self):
        return self.driver.current_url == HomePageData.HOME_PAGE_URL

    def filter_transactions(self, association):
        if association == "everyone":
            self.do_click(self.FILTER_BY_ASSOCIATION_EVERYONE_BTN)
        if association == "friends":
            self.do_click(self.FILTER_BY_ASSOCIATION_FRIENDS_BTN)
        if association == "mine":
            self.do_click(self.FILTER_BY_ASSOCIATION_MINE_BTN)

    def get_welcome_inscription_text(self):
        text = self.get_element_text(self.WELCOME_INSCRIPTION)
        return text

