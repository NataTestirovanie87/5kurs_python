from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class CheckoutPage:
    def __init__(self, driver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Заполнить информацию о покупателе")
    def fill_in_customer_info(
        self,
        first_name: str,
        last_name: str,
        postal_code: int
    ) -> None:
        """
        Заполняет поля формы с информацией о покупателе.
        """
        with allure.step("Заполнить поле 'First Name'"):
            self.wait.until(
                EC.presence_of_element_located(
                    (By.ID, "first-name"))).send_keys(first_name)
        with allure.step("Заполнить поле 'Last Name'"):
            last_name_field = self.driver.find_element(By.ID, "last-name")
            last_name_field.send_keys(last_name)

        with allure.step("Заполнить поле 'Postal Code'"):
            postal_code_field = self.driver.find_element(By.ID, "postal-code")
            postal_code_field.send_keys(postal_code)

    @allure.step("Нажать кнопку 'Continue' для продолжения оформления заказа")
    def continue_checkout(self) -> None:
        """
        Нажатие кнопки продолжения оформления заказа.
        """
        continue_button = self.driver.find_element(By.ID, "continue")
        continue_button.click()

    @allure.step("Получить итоговую сумму из страницы")
    def get_total_amount(self) -> str:
        """
        Возвращает текст итоговой суммы заказа.
        """
        total_element = self.wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, ".summary_total_label")))
        return total_element.text.strip()
