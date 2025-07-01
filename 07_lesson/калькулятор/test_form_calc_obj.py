import pytest
from selenium import webdriver
from FormCalcPage import CalculatorPage


@pytest.fixture
def driver():
    driver_instance = webdriver.Chrome()
    driver_instance.maximize_window()
    yield driver_instance
    driver_instance.quit()


def test_slow_calculator(driver):
    calculator_page = CalculatorPage(driver)
    calculator_page.open()
    calculator_page.set_delay(45)
    calculator_page.click_button('7')
    calculator_page.click_button('+')
    calculator_page.click_button('8')
    calculator_page.click_button('=')
    result_text = calculator_page.get_result_text("15")
    assert result_text == "15", f"Ожидалось '15', получено '{result_text}'"
