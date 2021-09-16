from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class HomePage:
    __SIGN_IN_BUTTON = (By.CSS_SELECTOR, "a[ggloginbutton]")
    __LOGIN_FORM = (By.CSS_SELECTOR, "form[name='loginform']")
    __USER_NAME_INPUT = (By.CSS_SELECTOR, "#inputUsername")
    __PASSWORD = (By.CSS_SELECTOR, "#inputPassword")
    __SUBMIT = (By.CSS_SELECTOR, "button[type='submit']")
    __ERROR_MESSAGE = (By.CSS_SELECTOR, "span.help-block")

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 3)

    def open_home_page(self):
        self.driver.get("https://boardgamegeek.com/")

    def navigate_to_login(self):
        self.driver.find_element(*self.__SIGN_IN_BUTTON).click()

    def login_user(self, user_name: str, user_password: str):
        login_form = self.driver.find_element(*self.__LOGIN_FORM)
        login_form.find_element(*self.__USER_NAME_INPUT).send_keys(user_name)
        login_form.find_element(*self.__PASSWORD).send_keys(user_password)
        login_form.find_element(*self.__SUBMIT).click()

    def get_error_message(self) -> str:
        error_message = self.driver.find_element(*self.__LOGIN_FORM).find_element(*self.__ERROR_MESSAGE)
        self.wait.until(lambda _: error_message.text != "")
        return self.driver.find_element(*self.__LOGIN_FORM).find_element(*self.__ERROR_MESSAGE).text

    def get_empty_error_message(self) -> str:
        error_message = self.driver.find_element(*self.__LOGIN_FORM).find_element(*self.__ERROR_MESSAGE)
        self.wait.until(lambda _: error_message.text == "")
        return self.driver.find_element(*self.__LOGIN_FORM).find_element(*self.__ERROR_MESSAGE).text
