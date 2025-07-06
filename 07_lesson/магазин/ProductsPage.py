from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductsPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_product_to_cart(self, product_id):
        add_button_locator = (By.ID, f"add-to-cart-{product_id}")
        self.wait.until(EC.element_to_be_clickable(add_button_locator)).click()

    def go_to_cart(self):
        cart_link_locator = (By.CSS_SELECTOR, ".shopping_cart_link")
        self.wait.until(EC.element_to_be_clickable(cart_link_locator)).click()
