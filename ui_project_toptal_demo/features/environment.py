from features.browser import Browser
from features.pages.base_page import BasePage
from features.pages.login_page import LoginPage
from features.pages.home_page import Homepage
from features.pages.shopping_cart_page import ShoppingCart


def before_all(context):
    context.browser = Browser()
    context.base_page = BasePage()
    context.login_page = LoginPage()
    context.home_page = Homepage()
    context.shopping_cart_page = ShoppingCart()


def after_all(context):
    context.browser.close()
