from studiu_echipa_S14.browser import Browser
from studiu_echipa_S14.pages.base_page import BasePage
from studiu_echipa_S14.pages.main_menu_link_page import MainMenuLinkPage
from studiu_echipa_S14.pages.sort_function_page import SortFunctionPage


def before_all(context):
    context.browser = Browser()
    context.base_page = BasePage()
    context.sort_function_page = SortFunctionPage()
    context.main_menu_link_page = MainMenuLinkPage()


def after_all(context):
    context.browser.close()
