import pytest
from pages.sign_in_page import SignInPage
from tests.test_sign_in.data import SignInData


@pytest.fixture
def home_tab(driver):
    sign_in_page = SignInPage(driver)
    home_tab = sign_in_page.do_login(SignInData.USERNAME, SignInData.PASSWORD)
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


def test_filter_transactions_by_friends(home_tab):
    home_tab.filter_transactions("friends")
    text = home_tab.get_element_text(home_tab.CHOSEN_ASSOCIATION_TEXT_DIV)
    assert text == "Contacts"


def test_filter_transactions_by_everyone(home_tab):
    home_tab.filter_transactions("everyone")
    text = home_tab.get_element_text(home_tab.CHOSEN_ASSOCIATION_TEXT_DIV)
    assert text == "Public"


def test_filter_transactions_by_mine(home_tab):
    home_tab.filter_transactions("mine")
    text = home_tab.get_element_text(home_tab.CHOSEN_ASSOCIATION_TEXT_DIV)
    assert text == "Personal"
