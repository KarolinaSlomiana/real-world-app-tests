import pytest
from assets.data import TestData
from pages.sign_in_page import SignInPage
from pages.bank_accounts.create_bank_account_form import CreateBankAccount


@pytest.fixture
def bank_accounts_tab(driver):
    sign_in_page = SignInPage(driver)
    main_page = sign_in_page.do_login(TestData.USERNAME, TestData.PASSWORD)
    bank_accounts_tab = main_page.go_to_bank_accounts_tab()

    return bank_accounts_tab


@pytest.fixture
def create_bank_account_form(driver):
    create_bank_account_form = CreateBankAccount(driver)

    return create_bank_account_form


def test_create_new_bank_account(bank_accounts_tab, create_bank_account_form):
    bank_accounts_tab.open_create_bank_account_form()
    create_bank_account_form.create_bank_account(TestData.BANK_NAME, TestData.BANK_ROUT_NUM, TestData.BANK_ACC_NUM)
    assert bank_accounts_tab.is_at()
    assert TestData.BANK_NAME in bank_accounts_tab.driver.page_source
