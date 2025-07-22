from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class CartPage:
    def __init__(self, driver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Перейти к оформлению заказа")
    def proceed_to_checkout(self) -> None:
        """
        Метод для перехода к оформлению заказа.
        Ожидает, пока кнопка 'checkout' станет кликабельной, и кликает по ней.
        """
        checkout_button_locator = (By.ID, "checkout")
        self.wait.until(
            EC.element_to_be_clickable(checkout_button_locator)).click()
