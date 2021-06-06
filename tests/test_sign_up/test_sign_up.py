import pytest
from tests.test_sign_up.data import SignUpData
from pages.sign_in_page import SignInPage
from pages.sign_up_page import SignUpPage


@pytest.fixture
def sign_in_page(driver):
    sign_in_page = SignInPage(driver)
    sign_in_page.go_to_sign_up_page()
    return sign_in_page


@pytest.fixture
def sign_up_page(driver):
    sign_up_page = SignUpPage(driver)
    return sign_up_page


def test_invalid_password(sign_up_page, sign_in_page):
    sign_up_page.do_sign_up(SignUpData.NEW_USER_FIRST_NAME,
                            SignUpData.NEW_USER_LAST_NAME,
                            SignUpData.NEW_USER_USERNAME, 'jjj', 'jjj')
    assert 'Password must contain at least 4 characters' == sign_up_page.get_incorrect_password_text()


def test_different_password_confirmation(sign_up_page, sign_in_page):
    sign_up_page.do_sign_up(SignUpData.NEW_USER_FIRST_NAME,
                            SignUpData.NEW_USER_LAST_NAME,
                            SignUpData.NEW_USER_USERNAME,
                            SignUpData.NEW_USER_PASSWORD, 'kkk')
    assert 'Password does not match' == sign_up_page.get_different_password_confirmation_text()


def test_signup(sign_up_page, sign_in_page):
    sign_up_page.do_sign_up(SignUpData.NEW_USER_FIRST_NAME,
                            SignUpData.NEW_USER_LAST_NAME,
                            SignUpData.NEW_USER_USERNAME,
                            SignUpData.NEW_USER_PASSWORD,
                            SignUpData.NEW_USER_PASSWORD)
    home_tab = sign_in_page.do_login(SignUpData.NEW_USER_USERNAME, SignUpData.NEW_USER_PASSWORD)
    assert 'Get Started with Real World App' == home_tab.get_welcome_inscription_text()

