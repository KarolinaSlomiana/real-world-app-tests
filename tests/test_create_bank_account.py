import pytest
from assets.data import TestData
from pages.sign_in_page import SignInPage


@pytest.fixture
def bank_accounts_tab(driver):
    sign_in_page = SignInPage(driver)
    main_page = sign_in_page.do_login("Katharina_Bernier", "s3cret")
    bank_accounts_tab = main_page.go_to_bank_accounts_tab()

    return bank_accounts_tab


def test_create_new_bank_account(bank_accounts_tab, create_bank_account_form):
    bank_accounts_tab.open_create_bank_account_form()
    create_bank_account_form.create_bank_account(TestData.BANK_NAME, TestData.BANK_ROUT_NUM, TestData.BANK_ACC_NUM)
    assert bank_accounts_tab.is_at()
    assert TestData.BANK_NAME in bank_accounts_tab.page_source
