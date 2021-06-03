import pytest
from assets.data import TestData
from pages.sign_in_page import SignInPage


@pytest.fixture
def new_transaction_tab(driver):
    sign_in_page = SignInPage(driver)
    main_page = sign_in_page.do_login(TestData.USERNAME, TestData.PASSWORD)
    new_transaction_tab = main_page.go_to_new_transaction_tab()
    return new_transaction_tab


def test_make_new_payment_request(new_transaction_tab):
    new_transaction_tab.choose_nth_item_in_the_contact_list(TestData.TRANSACTION_CONTACT_POSITION)
    new_transaction_tab.choose_amount(TestData.TRANSACTION_AMOUNT)
    new_transaction_tab.write_note(TestData.TRANSACTION_NOTE)
    new_transaction_tab.submit_payment_request()

    assert new_transaction_tab.is_at()
    assert f"Requested ${'{0:.2f}'.format(TestData.TRANSACTION_AMOUNT)} for {TestData.TRANSACTION_NOTE}" \
           in new_transaction_tab.driver.page_source


def test_make_new_payment(new_transaction_tab):
    new_transaction_tab.choose_nth_item_in_the_contact_list(TestData.TRANSACTION_CONTACT_POSITION)
    new_transaction_tab.choose_amount(TestData.TRANSACTION_AMOUNT)
    new_transaction_tab.write_note(TestData.TRANSACTION_NOTE)
    new_transaction_tab.submit_payment()

    assert new_transaction_tab.is_at()
    assert f"Paid ${'{0:.2f}'.format(TestData.TRANSACTION_AMOUNT)} for {TestData.TRANSACTION_NOTE}" \
           in new_transaction_tab.driver.page_source
