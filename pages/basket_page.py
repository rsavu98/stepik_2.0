from pages.base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):
    def click_view_busket_btn(self):
        self.browser.find_element(*BasketPageLocators.VIEW_BASKET_BTN).click()

    def is_basket_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "Basket is not empty"

    def backet_is_empty_text_displayed(self):
        assert "Your basket is empty." in self.browser.find_element(*BasketPageLocators.BASKET_IS_EMPTY_TEXT).text, \
            "Backet is not empty"