from pages.base_page import BasePage


class MyAccount(BasePage):
    def __init__(self, driver) -> None:
        super().__init__(driver)

    def is_at(self):
        return self.driver.current_url.endswith("/user/settings")

    def change_first_name(self, first_name):
        self.driver.find_element_by_id("user-settings-firstName-input").clear()
        self.driver.find_element_by_id("user-settings-firstName-input").send_keys(first_name)
        self.driver.find_element_by_css_selector("button.MuiButton-root > span:nth-child(1)").click()

    def change_last_name(self, last_name):
        self.driver.find_element_by_id("user-settings-lastName-input").clear()
        self.driver.find_element_by_id("user-settings-lastName-input").send_keys(last_name)
        self.driver.find_element_by_css_selector("button.MuiButton-root > span:nth-child(1)").click()

    def change_email(self, email):
        self.driver.find_element_by_id("user-settings-email-input").clear()
        self.driver.find_element_by_id("user-settings-email-input").send_keys(email)
        self.driver.find_element_by_css_selector("button.MuiButton-root > span:nth-child(1)").click()

    def change_phone_number(self, phone_number):
        self.driver.find_element_by_id("user-settings-phoneNumber-input").clear()
        self.driver.find_element_by_id("user-settings-phoneNumber-input").send_keys(phone_number)
        self.driver.find_element_by_css_selector("button.MuiButton-root > span:nth-child(1)").click()