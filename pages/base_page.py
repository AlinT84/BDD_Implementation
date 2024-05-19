from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from studiu_echipa_S14.browser import Browser


class BasePage(Browser):

    def find(self, locator):
        return self.driver.find_element(*locator)

    def elements_are_present(self, locator, number_seconds):
        wait = WebDriverWait(self.driver, number_seconds)
        return wait.until(EC.presence_of_all_elements_located(locator))

    def element_is_visible(self, locator, number_seconds):
        wait = WebDriverWait(self.driver, number_seconds)
        return wait.until(EC.visibility_of_element_located(locator))

    def wait_for_page_load(self, timeout=30):
        """
        Wait for the page to load completely.

        Parameters:
            timeout (optional): Maximum time to wait for the page to load, in seconds. Default is 30 seconds.
        """
        WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )

    def click(self, locator):
        self.find(locator).click()

    def type(self, locator, text):
        self.find(locator).send_keys(text)
