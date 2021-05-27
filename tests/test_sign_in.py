import pytest
from assets.data import TestData
from pages.sign_in_page import SignInPage
from pages.sign_up_page import SignUpPage


@pytest.fixture
def pages(driver):
    sign_in_page = SignInPage(driver)
    sign_up_page = SignUpPage(driver)
    return [sign_in_page, sign_up_page]


def test_links_works(pages):
    sign_in_page = pages[0]
    sign_up_page = sign_in_page.go_to_sign_up_page()
    assert sign_up_page.get_element_text(sign_up_page.SIGN_IN_LINK) == 'Have an account? Sign In'
    sign_up_page.go_to_sign_in_page()
    assert sign_in_page.get_element_text(sign_in_page.SIGN_UP_LINK) == "Don't have an account? Sign Up"


def test_login_incorrect_credentials(sign_in_page):
    sign_in_page.do_login(TestData.FIRST_NAME, TestData.USERNAME)
    text = sign_in_page.get_element_text(sign_in_page.INCORRECT_CREDENTIALS_MESSAGE)
    assert "Username or password is invalid" == text


def test_login(pages):
    sign_in_page = pages[0]
    sign_up_page = sign_in_page.go_to_sign_up_page()
    sign_up_page.do_sign_up(TestData.FIRST_NAME,
                            TestData.LAST_NAME,
                            TestData.USERNAME,
                            TestData.PASSWORD,
                            TestData.PASSWORD)
    home = sign_in_page.do_login(TestData.USERNAME, TestData.PASSWORD)
    assert 'Get Started with Real World App' == home.get_element_text(home.WELCOME_INSCRIPTION)