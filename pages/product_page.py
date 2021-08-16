from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):

    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN).click()

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def is_product_price_in_basket_correct(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_BASKET).text == self.get_product_price(),\
            "Product price in basket is incorrect"

    def is_product_name_in_basket_correct(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_BASKET).text == self.get_product_name(), \
            "Product name added in basket is incorrect"

    def is_success_message_present(self):
        self.browser.is_not_element_present(*ProductPageLocators.PRODUCT_NAME_IN_BASKET)
