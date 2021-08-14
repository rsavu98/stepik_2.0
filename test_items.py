import time


def test_add_to_basket_btn_present(browser):

    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)

    # time.sleep(5)

    add_to_basket_btn = browser.find_element_by_css_selector('.btn-add-to-basket')
    assert add_to_basket_btn.is_displayed(), "Add to basket button is not displayed"
