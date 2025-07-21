import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.feature("Calculator Page")
class CalculatorPage:
    """
    Страница калькулятора, реализующая взаимодействие с элементами страницы.
    """

    def __init__(self, driver) -> None:
        """
        Инициализация страницы.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)

    # Локаторы элементов страницы
    DELAY_INPUT = (By.CSS_SELECTOR, "#delay")
    BUTTON_TEMPLATE = "//span[.='{}']"
    RESULT_SCREEN = (By.CSS_SELECTOR, ".screen")

    @allure.step("Открыть страницу калькулятора")
    def open(self) -> None:
        """
        Открывает страницу калькулятора в браузере.
        """
        self.driver.get(
            "https:"
            "//bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        )

    @allure.step("Установить задержку равную {seconds} секундам")
    def set_delay(self, seconds: int) -> None:
        """
        Устанавливает задержку перед выполнением операций.
        """
        delay_element = self.wait.until(
            EC.presence_of_element_located(self.DELAY_INPUT)
        )
        delay_element.clear()
        delay_element.send_keys(str(seconds))

    @allure.step("Нажать кнопку с меткой '{label}'")
    def click_button(self, label: str) -> None:
        """
        Нажимает на кнопку с указанной меткой.
        """
        button_locator = (By.XPATH, self.BUTTON_TEMPLATE.format(label))
        button_element = self.wait.until(
            EC.element_to_be_clickable(button_locator)
        )
        button_element.click()

    @allure.step("Получить текст результата: '{text}'")
    def get_result_text(self, text: str) -> str:
        """
        Проверяет наличие текста в области результата
        и возвращает текущий текст.
        """
        self.wait.until(
            EC.text_to_be_present_in_element(self.RESULT_SCREEN, text)
        )
        result_element = self.driver.find_element(*self.RESULT_SCREEN)
        return result_element.text.strip()
