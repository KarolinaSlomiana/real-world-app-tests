from pages.base_page import BasePage


class NewTransaction(BasePage):

    # locators
    # SELECT_CONTACT_SEARCH_INPUT = (By.ID, 'user-list-search-input')

    def __init__(self, driver) -> None:
        super().__init__(driver)

    def is_at(self):
        return self.driver.current_url.endswith("/transaction/new")

    def make_new_payment(self, item_in_the_contact_list, amount, note):
        self.driver.find_element_by_css_selector("li.MuiListItem-root:nth-child(%i)" % item_in_the_contact_list).click()
        self.driver.find_element_by_id("amount").send_keys(amount)
        self.driver.find_element_by_id("transaction-create-description-input").send_keys(note)
        self.driver.find_element_by_css_selector("div.MuiGrid-container:nth-child(3) > div:nth-child(2) >"
                                                 " button:nth-child(1)").click()

    def request_payment(self, item_in_the_contact_list, amount, note):
        self.driver.find_element_by_css_selector("li.MuiListItem-root:nth-child(%i)" % item_in_the_contact_list).click()
        self.driver.find_element_by_id("amount").send_keys(amount)
        self.driver.find_element_by_id("transaction-create-description-input").send_keys(note)
        self.driver.find_element_by_css_selector("div.MuiGrid-container:nth-child(3) > div:nth-child(1) >"
                                                 " button:nth-child(1)").click()

