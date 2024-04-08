from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class BasePage:

    def __init__(self, frequency=2, timeout=10):
        # Define desired capabilities
        self.desired_caps = {
            "platformName": "Android",
            "platformVersion": "your_android_version",
            "deviceName": "your_device_name",
            "appPackage": "your_app_package",
            "appActivity": "your_app_activity"
        }

        # Start the Appium server and connect to the device
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", self.desired_caps)

        # Set frequency and timeout
        self.frequency = frequency
        self.timeout = timeout

    def enter_text(self, locator, text):
        temperature_element = WebDriverWait(self.driver, self.timeout, poll_frequency=self.frequency).until(
            EC.visibility_of_element_located(locator))
        temperature_element.send_keys(text)

    def get_element_text(self, locator):
        return WebDriverWait(self.driver, self.timeout, poll_frequency=self.frequency).until(
            EC.visibility_of_element_located(locator))

    def close_driver(self):
        # Close the driver session
        self.driver.quit()
