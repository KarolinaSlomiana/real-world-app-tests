from pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, driver) -> None:
        super().__init__(driver)

    def is_at(self):
        return self.driver.current_url

    def filter_transactions(self, association, date, amount):
        if association == "everyone":
            self.driver.find_element_by_css_selector("a.MuiTab-root:nth-child(1)").click()
        if association == "friends":
            self.driver.find_element_by_css_selector("a.MuiTab-root:nth-child(2)").click()
        if association == "mine":
            self.driver.find_element_by_css_selector("a.MuiTab-root:nth-child(3)").click()
        self.driver.find_element_by_css_selector("div.MuiGrid-spacing-xs-1:nth-child(1) > div:nth-child(1) > "
                                                 "div:nth-child(1) > div:nth-child(1)").click()
        self.driver.find_element_by_css_selector(".Cal__Container__root").send_keys(date)
        self.driver.find_element_by_css_selector("div.MuiGrid-spacing-xs-1:nth-child(1) > div:nth-child(2) > "
                                                 "div:nth-child(1) > div:nth-child(1)")
        self.driver.find_element_by_css_selector(".makeStyles-amountRangeRoot-575").send_keys(amount)


