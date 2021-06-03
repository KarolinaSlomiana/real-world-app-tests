import pytest
from assets.data import TestData
from pages.sign_in_page import SignInPage
from pages.sign_up_page import SignUpPage


@pytest.fixture
def pages(driver):
    sign_in_page = SignInPage(driver)
    sign_in_page.go_to_sign_up_page()
    sign_up_page = SignUpPage(driver)
    return [sign_in_page, sign_up_page]


def test_invalid_password(pages):
    sign_up_page = pages[1]
    sign_up_page.do_sign_up(TestData.NEW_USER_FIRST_NAME, TestData.NEW_USER_LAST_NAME, TestData.NEW_USER_USERNAME,
                            TestData.INVALID_SHORT_PASSWORD, TestData.INVALID_SHORT_PASSWORD)
    text = sign_up_page.get_element_text(sign_up_page.PASSWORD_HELPER_TEXT)
    assert 'Password must contain at least 4 characters' == text


def test_different_password_confirmation(pages):
    sign_up_page = pages[1]
    sign_up_page.do_sign_up(TestData.NEW_USER_FIRST_NAME, TestData.NEW_USER_LAST_NAME, TestData.NEW_USER_USERNAME,
                            TestData.NEW_USER_PASSWORD, TestData.INVALID_PASSWORD)
    assert 'Password does not match' == sign_up_page.get_element_text(sign_up_page.CONFIRM_PASSWORD_HELPER_TEXT)


def test_signup(pages):
    sign_up_page = pages[1]
    sign_up_page.do_sign_up(TestData.NEW_USER_FIRST_NAME,
                            TestData.NEW_USER_LAST_NAME,
                            TestData.NEW_USER_USERNAME,
                            TestData.NEW_USER_PASSWORD,
                            TestData.NEW_USER_PASSWORD)
    sign_in_page = pages[0]
    assert "Don't have an account? Sign Up" == sign_in_page.get_element_text(sign_in_page.SIGN_UP_LINK)
