import pytest
from web_gui_appium.temperature_page import TemperaturePage


# Fixture to initialize the web driver
@pytest.fixture(scope="module")
def web_driver():
    # Initialize the TemperaturePage object
    web_driver = TemperaturePage()
    yield web_driver  # yield the web driver object for the test
    # Teardown: Close the web driver after the test completes
    web_driver.close_driver()


# Test function to change and check temperature
@pytest.mark.parametrize("temperature", ["20", "21", "25"])
def test_change_and_check_temperature(web_driver, temperature):
    expected_temperature = temperature  # Expected temperature value
    # Set the temperature using the web driver
    web_driver.set_temepature(expected_temperature)
    # Get the displayed temperature element using the web driver
    displayed_temperature_element = web_driver.get_temepature()

    # Assertion: Check if displayed temperature matches expected temperature
    assert displayed_temperature_element.text == expected_temperature, "Displayed temperature does not match expected temperature."
