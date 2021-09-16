import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from pages.home_page import HomePage


@pytest.fixture
def driver():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(5)
    yield driver
    driver.close()
    driver.quit()


@pytest.fixture
def home_page(driver):
    home_page = HomePage(driver)
    return home_page


@pytest.fixture
def user_invalid_credentials() -> tuple:
    return "niematakiegokonta", "niematakiegohasla"


@pytest.fixture
def user_credentials() -> tuple:
    return "ssj4", "qweasdzxc"


def test_fail_login(home_page, user_invalid_credentials):
    home_page.open_home_page()
    home_page.navigate_to_login()
    home_page.login_user(*user_invalid_credentials)
    assert home_page.get_error_message() == "Invalid username or password"


def test_login(home_page, user_credentials):
    home_page.open_home_page()
    home_page.navigate_to_login()
    home_page.login_user(*user_credentials)
