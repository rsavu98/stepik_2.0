from pages.basket_page import BasketPage
from pages.locators import ProductPageLocators
from pages.login_page import LoginPage
from pages.product_page import ProductPage
import pytest
import time
from random import randrange

link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"

@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.is_product_name_in_basket_correct()
    page.is_product_price_in_basket_correct()

def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.is_not_element_present(*ProductPageLocators.PRODUCT_NAME_IN_BASKET)


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = BasketPage(browser, link)
    page.open()
    page.click_view_busket_btn()
    page.is_basket_empty()
    page.backet_is_empty_text_displayed()


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function")
    def setup(self, browser):
        self.login_page = LoginPage(browser, "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/")
        self.link = self.login_page.url
        self.login_page.open()
        self.login_page.register_new_user(str(time.time()) + "@fakemail.org", randrange(10**10))
        self.login_page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser, setup):
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        page.is_product_name_in_basket_correct()
        page.is_product_price_in_basket_correct()

    @pytest.mark.xfail
    def test_user_cant_see_success_message_after_adding_product_to_basket(self, browser, setup):
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        page.is_not_element_present(*ProductPageLocators.PRODUCT_NAME_IN_BASKET)





