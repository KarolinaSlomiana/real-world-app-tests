import pytest

from pages.home_page import HomePage


@pytest.fixture
def home_page(driver):
    return HomePage(driver)

# fixture user logged in


def test_navigate_to_new_transaction_tab_and_back(home_page):
    new_transaction_tab = home_page.go_to_new_transaction_tab()
    assert new_transaction_tab.is_at()

    home_page = new_transaction_tab.cancel()
    assert home_page.is_at()
