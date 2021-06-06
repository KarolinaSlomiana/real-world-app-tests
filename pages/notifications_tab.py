from pages.main_layout import MainPage


class Notifications(MainPage):
    def __init__(self, driver) -> None:
        super().__init__(driver)

    def is_at(self):
        return self.driver.current_url.endswith("/notifications")

    def dismiss_notification(self, item_in_the_list):
        self.driver.find_element_by_css_selector("li.MuiListItem-root:nth-child(%i) > button:nth-child(3)"
                                                 % item_in_the_list).click()
