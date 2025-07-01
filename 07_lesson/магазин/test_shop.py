import pytest
from selenium import webdriver
from LoginPage import LoginPage
from ProductsPage import ProductsPage
from CartPage import CartPage
from CheckoutPage import CheckoutPage


@pytest.fixture
def driver():
    driver_instance = webdriver.Firefox()
    driver_instance.maximize_window()
    yield driver_instance
    driver_instance.quit()


def test_purchase_flow(driver):
    login_page = LoginPage(driver)
    products_page = ProductsPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    driver.get("https://www.saucedemo.com/")
    login_page.login("standard_user", "secret_sauce")
    products_to_add = [
        "sauce-labs-backpack",
        "sauce-labs-bolt-t-shirt",
        "sauce-labs-onesie"
    ]
    for product_id in products_to_add:
        products_page.add_product_to_cart(product_id)

    products_page.go_to_cart()
    cart_page.proceed_to_checkout()
    checkout_page.fill_in_customer_info("Наталья", "Шабардина", "456440")
    checkout_page.continue_checkout()
    total_text = checkout_page.get_total_amount()

    assert "$58.29" in total_text, f"Ожидали $58.29, получили: {total_text}"
