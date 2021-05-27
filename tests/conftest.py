from selenium.webdriver import Chrome
from selenium.webdriver import Firefox

import pytest
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture
def base_url():
    return 'http://localhost:3000'


@pytest.fixture
def driver(base_url, browser='Chrome'):
    driver = _chrome_driver() if browser == 'Chrome' else _firefox_driver()
    driver.implicitly_wait(2)
    driver.get(base_url)
    yield driver
    driver.quit()


def _chrome_driver():
    return Chrome(ChromeDriverManager().install())


def _firefox_driver():
    return Firefox(executable_path=GeckoDriverManager().install())
