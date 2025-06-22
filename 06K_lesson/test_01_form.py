import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.test_color_field
def test_form_field_colors():
    # Инициализация драйвера Edge
    driver = webdriver.Edge(
        service=EdgeService(EdgeChromiumDriverManager().install())
        )
    try:
        wait = WebDriverWait(driver, 20)
        driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

        # Ввод данных в поля формы
        form_data = {
            "first-name": "Иван",
            "last-name": "Петров",
            "address": "Ленина, 55-3",
            "e-mail": "test@skypro.com",
            "phone": "+7985899998787",
            "zip-code": "",
            "city": "Москва",
            "country": "Россия",
            "job-position": "QA",
            "company": "SkyPro"
        }

        for name_attr, value in form_data.items():
            waiter_element = wait.until(
                EC.element_to_be_clickable((By.NAME, name_attr))
            )
            waiter_element.clear()
            waiter_element.send_keys(value)

        # Нажимаем кнопку Submit
        button = wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "btn-outline-primary"))
        )
        driver.execute_script("arguments[0].click();", button)

        # Ожидание появления элементов после отправки формы
        selectors = [
            "#first-name",
            "#last-name",
            "#address",
            "#e-mail",
            "#phone",
            "#zip-code",
            "#city",
            "#country",
            "#job-position",
            "#company"
        ]

        for selector in selectors:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))

        # Проверка цвета фона поля zip-code (ожидается красный)
        zip_code_element = driver.find_element(By.CSS_SELECTOR, "#zip-code")
        bg_color_zip = zip_code_element.value_of_css_property(
            "background-color")
        expected_red_bg = "rgba(248, 215, 218, 1)"  # #f8d7da

        assert bg_color_zip == expected_red_bg, (
            f"Цвет Полеполя zip-code{bg_color_zip}, ожидаем: {expected_red_bg}"
        )

        # Проверка цвета фона остальных полей (ожидается зеленый)
        green_bg_color = "rgba(209, 231, 221, 1)"  # #d1e7dd
        fields_selectors = [
            "#first-name",
            "#last-name",
            "#address",
            "#e-mail",
            "#phone",
            "#city",
            "#country",
            "#job-position",
            "#company"
        ]

        for selector in fields_selectors:
            element = driver.find_element(By.CSS_SELECTOR, selector)
            bg_color = element.value_of_css_property("background-color")
            assert bg_color == green_bg_color, (
                f"У поля {selector} цвет {bg_color}, ожидаем: {green_bg_color}"
            )
    finally:
        driver.quit()
