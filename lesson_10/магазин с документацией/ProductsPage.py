from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class ProductsPage:
    def __init__(self, driver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Добавить товар с ID '{product_id}' в корзину")
    def add_product_to_cart(self, product_id: int) -> None:
        """
        Добавляет товар с указанным ID в корзину.
        """
        add_button_locator = (By.ID, f"add-to-cart-{product_id}")
        self.wait.until(EC.element_to_be_clickable(add_button_locator)).click()

    @allure.step("Перейти в корзину")
    def go_to_cart(self) -> None:
        """
        Переходит на страницу корзины.
        """
        cart_link_locator = (By.CSS_SELECTOR, ".shopping_cart_link")
        self.wait.until(EC.element_to_be_clickable(cart_link_locator)).click()
