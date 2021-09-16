from .base_page import BasePage
from .locators import ProductPageLocators


class productPage(BasePage):
    def go_to_product_page(self):
        link = self.browser.find_element(*ProductPageLocators.BASKET_ADD_BUTTON)
        link.click()

    def should_be_message_add_to_basket(self):
        product_name = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT).text
        message = self.browser.find_element(*ProductPageLocators.MESSAGE_ADD_TO_BASKET_NAME_PRODUCT).text
        assert product_name in message, "No product name in message"

    def should_be_message_price_basket_total(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text
        message = self.browser.find_element(*ProductPageLocators.MESSAGE_PRICE_BASKET_TOTAL).text
        assert product_price in message, "No product price in message"