import pytest
from tests.test_sign_up.data import SignUpData
from tests.test_sign_in.data import SignInData
from pages.sign_in_page import SignInPage
from pages.sign_up_page import SignUpPage


@pytest.fixture
def sign_up_page(driver):
    sign_up_page = SignUpPage(driver)
    return sign_up_page


@pytest.fixture
def sign_in_page(driver):
    sign_in_page = SignInPage(driver)
    return sign_in_page


def test_links_works(sign_in_page):
    sign_up_page = sign_in_page.go_to_sign_up_page()
    assert sign_up_page.is_at()
    sign_up_page.go_to_sign_in_page()
    assert sign_in_page.is_at()


def test_login_incorrect_credentials(sign_in_page):
    sign_in_page.do_login(SignUpData.NEW_USER_PASSWORD, SignUpData.NEW_USER_PASSWORD)
    assert "Username or password is invalid" == sign_in_page.get_incorrect_credentials_text()


def test_login_existing_user(sign_in_page):
    main_page = sign_in_page.do_login(SignInData.USERNAME, SignInData.PASSWORD)
    text = main_page.get_avatar_name_text()
    assert 'Edgar J' == text
