from pages.base_page import BasePage


class LoginPage(BasePage):
    # INCORRECT_CREDENTIALS_MESSAGE = (By.CSS_SELECTOR, ".MuiAlert-message")
    def __init__(self, driver) -> None:
        super().__init__(driver)

    def is_at(self):
        return self.driver.current_url.endswith("/signin")

    def do_login(self, username, password):
        self.driver.find_element_by_id("username").clear()
        self.driver.find_element_by_id("username").send_keys(username)
        self.driver.find_element_by_id("password").clear()
        self.driver.find_element_by_id("password").send_keys(password)
        self.driver.find_element_by_css_selector("button.MuiButtonBase-root[tabindex='0']").click()
        from pages.home_page import HomePage
        return HomePage(self.driver)

    def go_to_signup_page(self):
        self.driver.find_element_by_css_selector(".MuiGrid-item > a").click()
        from pages.sign_up_page import SignupPage
        return SignupPage(self.driver)
