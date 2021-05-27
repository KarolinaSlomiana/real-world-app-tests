import pytest
from pages.sign_in_page import SignInPage


@pytest.fixture
def home_tab(driver):
    sign_in_page = SignInPage(driver)
    home_tab = sign_in_page.do_login("Katharina_Bernier", "s3cret")
    return home_tab


def test_navigate_to_new_transaction_tab_and_back(home_tab):
    new_transaction_tab = home_tab.go_to_new_transaction_tab()
    assert new_transaction_tab.is_at()

    home_tab = new_transaction_tab.go_to_home_tab()
    assert home_tab.is_at()


def test_navigate_to_my_account_tab_and_back(home_tab):
    my_account_tab = home_tab.go_to_my_account_tab()
    assert my_account_tab.is_at()

    home_tab = my_account_tab.go_to_home_tab()
    assert home_tab.is_at()


def test_navigate_to_bank_accounts_tab_and_back(home_tab):
    bank_accounts_tab = home_tab.go_to_bank_accounts_tab()
    assert bank_accounts_tab.is_at()

    home_tab = bank_accounts_tab.go_to_home_tab()
    assert home_tab.is_at()


def test_navigate_to_notifications_tab_and_back(home_tab):
    notifications_tab = home_tab.go_to_notifications_tab()
    assert notifications_tab.is_at()

    home_tab = notifications_tab.go_to_home_tab()
    assert home_tab.is_at()
