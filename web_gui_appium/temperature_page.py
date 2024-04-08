from selenium.webdriver.common.by import By
from base_page import BasePage

class Locator:
    TemperatureEditText = (By.ID, "temperatureEditText")
    DisplayTemperatureTextView = (By.ID, "displayTemperatureTextView")
class TemperaturePage(BasePage):
    def __init__(self):
        super().__init__()

    def set_temepature(self, temperature):
        self.enter_text(Locator.TemperatureEditText, temperature)

    def get_temepature(self):
        return self.get_element_text(Locator.DisplayTemperatureTextView)