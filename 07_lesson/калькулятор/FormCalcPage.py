from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)

    # Локаторы
    DELAY_INPUT = (By.CSS_SELECTOR, "#delay")
    BUTTON_TEMPLATE = "//span[.='{}']"
    RESULT_SCREEN = (By.CSS_SELECTOR, ".screen")

    # Методы для взаимодействия
    def open(self):
        self.driver.get(
            "https:"
            "//bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
            )

    def set_delay(self, seconds):
        delay_element = self.wait.until(
            EC.presence_of_element_located(self.DELAY_INPUT))
        delay_element.clear()
        delay_element.send_keys(str(seconds))

    def click_button(self, label):
        button_locator = (By.XPATH, self.BUTTON_TEMPLATE.format(label))
        button_element = self.wait.until(
            EC.element_to_be_clickable(button_locator))
        button_element.click()

    def get_result_text(self, text):
        self.wait.until(
            EC.text_to_be_present_in_element(self.RESULT_SCREEN, text))
        result_element = self.driver.find_element(*self.RESULT_SCREEN)
        return result_element.text.strip()
