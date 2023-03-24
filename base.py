from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout

    def _wait(self, locator, condition):
        return WebDriverWait(self.driver, self.timeout).until(
            condition(locator)
        )

    def find_element(self, locator):
        return self._wait(locator, EC.presence_of_element_located)

    def find_elements(self, locator):
        return self._wait(locator, EC.presence_of_element_located)

    def click(self, locator):
        self._wait(locator, EC.presence_of_element_located).click()

    def enter_text(self, locator, text):
        return self._wait(locator, EC.presence_of_element_located).send_keys(
            text
        )

    def check_url(self, value):
        return self._wait(value, EC.url_to_be)

    def get_attr(self, locator, attr):
        return self._wait(
            locator, EC.presence_of_element_located
        ).get_attribute(attr)

    def switch(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])
