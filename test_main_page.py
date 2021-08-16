from pages.basket_page import BasketPage
from pages.main_page import MainPage

link = "http://selenium1py.pythonanywhere.com/"


class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(browser):
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()

    def test_guest_should_see_login_link(browser):
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = BasketPage(browser, link)
    page.open()
    page.click_view_busket_btn()
    page.is_basket_empty()
    page.backet_is_empty_text_displayed()
