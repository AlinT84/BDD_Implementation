from selenium.webdriver.common.by import By
from studiu_echipa_S14.pages.base_page import BasePage


class MainMenuLinkPage(BasePage):
    MAIN_PAGE_URL = "https://www.emag.ro/"
    MAIN_PAGE_BUTTON = (By.XPATH, '//img[@alt="eMAG"]')
    ACCOUNT_BUTTON = (By.XPATH, '//a[@id="my_account"]')
    FAV_BUTTON = (By.XPATH, '//a[@id="my_wishlist"]')
    CART_BUTTON = (By.XPATH, '//a[@id="my_cart"]')
    OFERTA_ZILEI_BUTTON = (
    By.XPATH,
    '//ul[@class="nav navbar-nav navbar-left "]/li/a[@title="Oferta Zilei"]',
                    )
    GENIUS_DEALS_BUTTON = (
        By.XPATH,
        '//ul[@class="nav navbar-nav navbar-left "]/li/a[@title="Genius Deals"]',
    )
    GENIUS_BUTTON = (
        By.XPATH,
        '//ul[@class="nav navbar-nav navbar-left "]/li/a[@title="Genius"]',
    )
    CARD_IDEI_BUTTON = (
        By.XPATH,
        '//ul[@class="nav navbar-nav navbar-left "]/li/a[@title="Cardul cu milioane de idei"]',
    )
    RABLA_BUTTON = (
        By.XPATH,
        '//ul[@class="nav navbar-nav navbar-left "]/li/a[@title="Rabla"]',
    )
    OFERTE_EMAG_BUTTON = (
        By.XPATH,
        '//ul[@class="nav navbar-nav navbar-left "]/li/a[@title="Ofertele eMAG"]',
    )

    def go_to_main_page(self):
        self.driver.get(self.MAIN_PAGE_URL)

    def click_main_page_button(self):
        self.element_is_visible(self.MAIN_PAGE_BUTTON, 10)
        self.click(self.MAIN_PAGE_BUTTON)

    def test_main_page_logo_button(self):
        self.wait_for_page_load()
        returned_url = self.driver.current_url
        expected_url = self.MAIN_PAGE_URL
        assert (expected_url == returned_url), f"Invalid page redirection, expected: {expected_url}, received: {returned_url}"

    def click_account_button(self):
        self.element_is_visible(self.ACCOUNT_BUTTON, 10)
        self.click(self.ACCOUNT_BUTTON)

    def test_account_button(self):
        self.wait_for_page_load()
        returned_url = self.driver.current_url
        expected_url = "https://auth.emag.ro/user/login"
        assert (expected_url == returned_url), f"Invalid page redirection, expected: {expected_url}, received: {returned_url}"

    def click_favourites_button(self):
        self.element_is_visible(self.FAV_BUTTON, 10)
        self.click(self.FAV_BUTTON)

    def test_favourites_button(self):
        self.wait_for_page_load()
        returned_url = self.driver.current_url
        expected_url = "https://www.emag.ro/favorites?ref=ua_favorites"
        assert (expected_url == returned_url), f"Invalid page redirection, expected: {expected_url}, received: {returned_url}"

    def click_shopping_cart_button(self):
        self.element_is_visible(self.CART_BUTTON, 10)
        self.click(self.CART_BUTTON)

    def test_shopping_cart_button(self):
        self.wait_for_page_load()
        returned_url = self.driver.current_url
        expected_url = "https://www.emag.ro/cart/products?ref=cart"
        assert (expected_url == returned_url), f"Invalid page redirection, expected: {expected_url}, received: {returned_url}"

    def click_oferta_zilei_button(self):
        self.element_is_visible(self.OFERTA_ZILEI_BUTTON, 10)
        self.click(self.OFERTA_ZILEI_BUTTON)

    def test_oferta_zilei_button(self):
        self.wait_for_page_load()
        returned_url = self.driver.current_url
        expected_url = "https://www.emag.ro/lps/oferta-zilei"
        assert (expected_url in returned_url), f"Invalid page redirection, expected: {expected_url}, received: {returned_url}"

    def click_genius_deals_button(self):
        self.element_is_visible(self.GENIUS_DEALS_BUTTON, 10)
        self.click(self.GENIUS_DEALS_BUTTON)

    def test_genius_deals_button(self):
        self.wait_for_page_load()
        returned_url = self.driver.current_url
        expected_url = "https://www.emag.ro/label-campaign/genius-deals"
        assert (expected_url in returned_url), f"Invalid page redirection, expected: {expected_url}, received: {returned_url}"

    def click_genius_button(self):
        self.element_is_visible(self.GENIUS_BUTTON, 10)
        self.click(self.GENIUS_BUTTON)

    def test_genius_button(self):
        self.wait_for_page_load()
        returned_url = self.driver.current_url
        expected_url = "https://www.emag.ro/genius?ref=hdr_genius"
        assert (expected_url == returned_url), f"Invalid page redirection, expected: {expected_url}, received: {returned_url}"

    def click_card_idei_button(self):
        self.element_is_visible(self.CARD_IDEI_BUTTON, 10)
        self.click(self.CARD_IDEI_BUTTON)

    def test_card_idei_button(self):
        self.wait_for_page_load()
        returned_url = self.driver.current_url
        expected_url = "https://www.emag.ro/voucher/gift-card?ref=hdr_cardul-cu-milioane-de-idei#step-1"
        assert (expected_url == returned_url), f"Invalid page redirection, expected: {expected_url}, received: {returned_url}"

    def click_rabla_button(self):
        self.element_is_visible(self.RABLA_BUTTON, 10)
        self.click(self.RABLA_BUTTON)

    def test_rabla_button(self):
        self.wait_for_page_load()
        returned_url = self.driver.current_url
        expected_url = "https://www.emag.ro/lps/rabla-emag?ref=hdr_rabla"
        assert (expected_url == returned_url), f"Invalid page redirection, expected: {expected_url}, received: {returned_url}"

    def click_oferte_emag_button(self):
        self.element_is_visible(self.OFERTE_EMAG_BUTTON, 10)
        self.click(self.OFERTE_EMAG_BUTTON)

    def test_oferte_emag_button(self):
        self.wait_for_page_load()
        returned_url = self.driver.current_url
        expected_url = "https://www.emag.ro/nav/deals?ref=hdr_ofertele-emag"
        assert (expected_url == returned_url), f"Invalid page redirection, expected: {expected_url}, received: {returned_url}"
