from selenium.webdriver.common.by import By
from studiu_echipa_S14.pages.base_page import BasePage


class SortFunctionPage(BasePage):
    URL = "https://www.emag.ro/"
    SEARCH_FIELD = (By.ID, "searchboxTrigger")
    SEARCH_SELECTOR = (By.CLASS_NAME, "searchbox-submit-button")
    SEARCH_TERM = 'iphone 15 pro max'
    SORT_MENU = (By.CSS_SELECTOR, ".sort-control-btn")
    ASCENDING_ORDER_OPTION = (By.XPATH, '//a[text()="Pret crescator"]')
    DESCENDIND_ORDER_OPTION = (By.XPATH, '//a[text()="Pret descrescator"]')
    REVIEWS_NB_OPTION = (By.XPATH, '//a[text()="Nr. review-uri"]')
    PRICES = (
        By.XPATH,
        '//div[@class="page-container"]/descendant::p[@class="product-new-price"]',
    )
    REVIEWS_NB = (
        By.XPATH,
        '//div[@id="card_grid"]/descendant::span[@class="visible-xs-inline-block "]',
    )

    def go_to_main_page(self):
        self.driver.get(self.URL)

    def search_product(self):
        self.element_is_visible(self.SEARCH_FIELD, 10)
        self.find(self.SEARCH_FIELD).clear()
        self.type(locator=self.SEARCH_FIELD, text=self.SEARCH_TERM)
        self.click(self.SEARCH_SELECTOR)

    def click_sort_menu(self):
        self.element_is_visible(self.SORT_MENU, 10)
        self.click(self.SORT_MENU)

    def select_ascending_option(self):
        self.element_is_visible(self.ASCENDING_ORDER_OPTION, 10)
        self.click(self.ASCENDING_ORDER_OPTION)

    def assert_ascending_order(self):
        self.elements_are_present(self.PRICES, 10)
        # Extract product prices after sorting
        sorted_prices = self.extract_data_from_elements(self.PRICES, flow="prices")

        # Validate sorting order
        is_ascending = sorted(sorted_prices)

        # Assert that prices are in ascending order
        assert sorted_prices == is_ascending

    def select_descending_option(self):
        self.element_is_visible(self.ASCENDING_ORDER_OPTION, 10)
        self.click(self.ASCENDING_ORDER_OPTION)

    def assert_descending_order(self):
        self.elements_are_present(self.PRICES, 10)
        # Extract product prices after sorting
        sorted_prices = self.extract_data_from_elements(self.PRICES, flow="prices")

        # Validate sorting order
        is_descending = sorted(sorted_prices)

        # Assert that prices are in ascending order
        assert sorted_prices == is_descending

    def select_review_order(self):
        self.element_is_visible(self.REVIEWS_NB_OPTION, 10)
        self.click(self.REVIEWS_NB_OPTION)

    def assert_by_review_order(self):
        self.elements_are_present(self.REVIEWS_NB, 10)
        # Extract product prices after sorting
        sorted_prices_by_reviews = self.extract_data_from_elements(self.REVIEWS_NB, flow="numbers")

        # Validate sorting order
        is_sorted_prices_by_reviews = sorted(sorted_prices_by_reviews)

        # Assert that prices are in ascending order
        assert sorted_prices_by_reviews == is_sorted_prices_by_reviews

    def extract_data_from_elements(self, locator, flow="default"):
        """
        Extracts data from web elements based on the provided locator and flow.

        Parameters:
            self: The WebDriver instance controlling the browser.
            locator: A tuple representing the locator strategy (e.g., By.CSS_SELECTOR)
                             and the locator value (e.g., ".price").
            flow (optional): The specific flow for data extraction. Available options:
                - "default": Extracts raw text from elements.
                - "prices": Extracts prices, converts to float, and formats (removes "lei" and extra whitespace).
                - "numbers": Extracts numbers, removes parentheses, and converts to integer.

        Returns:
            A list containing extracted data (strings, floats, or integers).
        """
        # Wait for the presence of all elements matching the provided locator
        elements = self.elements_are_present(locator, 10)

        # List to store extracted data
        extracted_data = []

        # Conditional logic based on the specified flow
        if flow == "prices":
            for element in elements:
                # Extract and process price data and remove "lei" and extra whitespace
                price_text = element.text.lower().replace("lei", "").strip()

                # Split the price text into main and decimal parts
                main_part, _, decimal_part = price_text.partition(",")

                # Format the price using the main and decimal parts (as float)
                formatted_price = f"{main_part.replace('.', '')}.{decimal_part.strip()}"
                try:
                    price_value = float(formatted_price)
                    extracted_data.append(price_value)
                except ValueError:
                    print(f"Error converting price to float: '{price_text}'")
        elif flow == "numbers":
            for element in elements:
                # Extract and process number data
                # Example specific processing for numbers (remove parentheses and convert to int)
                number_text = element.text.strip().replace("(", "").replace(")", "")
                try:
                    number_value = int(number_text)
                    extracted_data.append(number_value)
                except ValueError:
                    print(f"Error converting number to int: '{number_text}'")
        else:
            # Default flow: extract raw text from elements
            for element in elements:
                # Extract raw text data
                extracted_data.append(element.text.strip())

        return extracted_data  # Return the list of extracted data
