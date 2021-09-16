from pages.base_page import BasePage
from pages.product_page import productPage


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = BasePage(browser, link)
    page.open()
    product = productPage(browser, link)
    product.go_to_product_page()
    page.solve_quiz_and_get_code()
    product.should_be_message_add_to_basket()
    product.should_be_message_price_basket_total()