from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class LoginPage:
    def __init__(self, driver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    @allure.step("Ввести имя пользователя: '{username}'")
    def enter_username(self, username: str) -> None:
        """
        Вводит имя пользователя в соответствующее поле.
        """
        username_field = self.wait.until(
            EC.presence_of_element_located(self.username_input)
        )
        username_field.clear()
        username_field.send_keys(username)

    @allure.step("Ввести пароль")
    def enter_password(self, password: str) -> None:
        """
        Вводит пароль в соответствующее поле.
        """
        password_field = self.driver.find_element(*self.password_input)
        password_field.clear()
        password_field.send_keys(password)

    @allure.step("Нажать кнопку входа")
    def click_login(self) -> None:
        """
        Нажимает кнопку входа.
        """
        login_btn = self.driver.find_element(*self.login_button)
        login_btn.click()

    @allure.step("Войти в систему с логином '{username}'")
    def login(self, username, password):
        """
        Выполняет полный процесс входа: ввод логина и пароля и клик по кнопке.
        """
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
