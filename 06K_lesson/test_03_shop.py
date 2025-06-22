import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.test_purchase
def test_checking_amount():
    # Инициализация драйвера Firefox
    driver = webdriver.Firefox()
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)

    try:
        # Открываем сайт магазина
        driver.get("https://www.saucedemo.com/")

        # Авторизация на сайте
        username_input = wait.until(
            EC.presence_of_element_located((By.ID, "user-name"))
            )
        password_input = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.ID, "login-button")
        username_input.send_keys("standard_user")
        password_input.send_keys("secret_sauce")
        login_button.click()

        # Добавляем товары в корзину
        add_backpack = wait.until(
            EC.element_to_be_clickable((
                By.ID, "add-to-cart-sauce-labs-backpack"))
            )
        add_bolt_tshirt = driver.find_element(
            By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"
            )
        add_onesie = driver.find_element(
            By.ID, "add-to-cart-sauce-labs-onesie")

        add_backpack.click()
        add_bolt_tshirt.click()
        add_onesie.click()

        # Переходим в корзину
        cart_link = wait.until(
            EC.element_to_be_clickable((
                By.CSS_SELECTOR, ".shopping_cart_link"))
            )
        cart_link.click()

        # Нажимаем Checkout
        checkout_button = wait.until(
            EC.element_to_be_clickable((By.ID, "checkout"))
            )
        checkout_button.click()

        # Заполняем форму данных
        first_name_input = wait.until(
            EC.presence_of_element_located((By.ID, "first-name"))
            )
        last_name_input = driver.find_element(By.ID, "last-name")
        postal_code_input = driver.find_element(By.ID, "postal-code")
        continue_button = driver.find_element(By.ID, "continue")

        first_name_input.send_keys("Наталья")
        last_name_input.send_keys("Шабардина")
        postal_code_input.send_keys("456440")
        continue_button.click()

        # Проверяем итоговую сумму
        total_element = wait.until(
            EC.presence_of_element_located((
                By.CSS_SELECTOR, ".summary_total_label"))
            )
        total_text = total_element.text.strip()

        # Проверяем сумму
        assert "$58.29" in total_text, f"Ожидаем $58.29, сумма: {total_text}"

    finally:
        driver.quit()
