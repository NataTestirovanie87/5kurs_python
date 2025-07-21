import pytest
import allure
from selenium import webdriver
from FormCalcPage import CalculatorPage


@pytest.fixture
def driver():
    """
    Фикстура для инициализации и закрытия драйвера браузера.
    """
    driver_instance = webdriver.Chrome()
    driver_instance.maximize_window()
    yield driver_instance
    driver_instance.quit()


@allure.title("Тест сложения двух чисел с задержкой 45 секунд")
@allure.description("Проверка корректности сложения 7+8 с паузой в 45 секунд.")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
def test_slow_calculator(driver):
    """
    Тест проверяет выполнение сложения 7 + 8
    с задержкой 45 секунд и проверяет результат.

    :param driver: WebDriver - фикстура для браузера.
    """
    calculator_page = CalculatorPage(driver)

    with allure.step("Открыть страницу калькулятора"):
        calculator_page.open()

    with allure.step("Установить задержку 45 секунд"):
        calculator_page.set_delay(45)

    with allure.step("Нажать кнопку '7'"):
        calculator_page.click_button('7')

    with allure.step("Нажать кнопку '+'"):
        calculator_page.click_button('+')

    with allure.step("Нажать кнопку '8'"):
        calculator_page.click_button('8')

    with allure.step("Нажать кнопку '='"):
        calculator_page.click_button('=')

    with allure.step("Проверить, что результат равен '15'"):
        result_text = calculator_page.get_result_text('15')
        assert result_text == '15', f"Ожидалось '15', получено '{result_text}'"
