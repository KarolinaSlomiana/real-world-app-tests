import pytest
from assets.data import TestData
from pages.sign_in_page import SignInPage


@pytest.fixture
def new_transaction_tab(driver):
    sign_in_page = SignInPage(driver)
    main_page = sign_in_page.do_login("Katharina_Bernier", "s3cret")
    new_transaction_tab = main_page.go_to_new_transaction_tab()
    return new_transaction_tab


def test_make_new_payment_request(new_transaction_tab):
    new_transaction_tab.choose_first_item_in_the_contact_list()
    new_transaction_tab.choose_amount(TestData.TRANSACTION_AMOUNT)
    new_transaction_tab.write_note(TestData.TRANSACTION_NOTE)
    new_transaction_tab.submit_payment_request()

    assert new_transaction_tab.is_at()
    assert "Requested $30.00 for Hello" in new_transaction_tab.page_source


def test_make_new_payment(new_transaction_tab):
    new_transaction_tab.choose_first_item_in_the_contact_list()
    new_transaction_tab.choose_amount(TestData.TRANSACTION_AMOUNT)
    new_transaction_tab.write_note(TestData.TRANSACTION_NOTE)
    new_transaction_tab.submit_payment()

    assert new_transaction_tab.is_at()
    assert "Paid $30.00 for Hello" in new_transaction_tab.page_source
