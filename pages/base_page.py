from selenium.webdriver.support import expected_conditions as EC
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

    def click(self, locator):
        self.find(locator).click()

    def type(self, locator, text):
        self.find(locator).send_keys(text)

    # def get_text(self, locator):
    #     return self.find(locator).text
