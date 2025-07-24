import pytest
from selenium import webdriver
from LoginPage import LoginPage
from ProductsPage import ProductsPage
from CartPage import CartPage
from CheckoutPage import CheckoutPage
import allure


@pytest.fixture
def driver():
    driver_instance = webdriver.Firefox()
    driver_instance.maximize_window()
    yield driver_instance
    driver_instance.quit()


@allure.title("Тест покупки с добавлением товаров и оформлением заказа")
@allure.description("Этот тест проверяет полный сценарий покупки")
@allure.feature("Покупка")
@allure.severity(allure.severity_level.CRITICAL)
def test_purchase_flow(driver):
    login_page = LoginPage(driver)
    products_page = ProductsPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    with allure.step("Открыть страницу входа и выполнить вход"):
        driver.get("https://www.saucedemo.com/")
        login_page.login("standard_user", "secret_sauce")

    products_to_add = [
        "sauce-labs-backpack",
        "sauce-labs-bolt-t-shirt",
        "sauce-labs-onesie"
    ]

    with allure.step("Добавить выбранные товары в корзину"):
        for product_id in products_to_add:
            products_page.add_product_to_cart(product_id)

    with allure.step("Перейти в корзину"):
        products_page.go_to_cart()

    with allure.step("Перейти к оформлению заказа"):
        cart_page.proceed_to_checkout()

    with allure.step("Заполнить инфо о покупателе: имя, фамилия, индекс"):
        checkout_page.fill_in_customer_info("Наталья", "Шабардина", "456440")

    with allure.step("Продолжить оформление заказа"):
        checkout_page.continue_checkout()

    with allure.step("Получить итоговую сумму и проверить правильность"):
        total_text = checkout_page.get_total_amount()

        assert "$58.29" in total_text, f"Ожидали $58.29,получили: {total_text}"
