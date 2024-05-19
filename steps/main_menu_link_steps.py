from behave import *


@given('user is on the Main Page')
def step_impl(context):
    context.main_menu_link_page.go_to_main_page()


@when('user clicks on the home logo button')
def step_impl(context):
    context.main_menu_link_page.click_main_page_button()


@then('user is redirected to the main page')
def step_impl(context):
    context.main_menu_link_page.test_main_page_logo_button()


@when('user clicks on the account button')
def step_impl(context):
    context.main_menu_link_page.click_account_button()


@then('user is redirected to the login page')
def step_impl(context):
    context.main_menu_link_page.test_account_button()


@when('user clicks on the favourites button')
def step_impl(context):
    context.main_menu_link_page.click_favourites_button()


@then('user is redirected to the user favourite products list')
def step_impl(context):
    context.main_menu_link_page.test_favourites_button()


@when('user clicks on the shopping cart button button')
def step_impl(context):
    context.main_menu_link_page.click_shopping_cart_button()


@then('user is redirected to the shopping cart page')
def step_impl(context):
    context.main_menu_link_page.test_shopping_cart_button()


@when('user clicks on the "Oferta zilei" button')
def step_impl(context):
    context.main_menu_link_page.click_oferta_zilei_button()


@then('user is redirected to the "Oferta zilei" page')
def step_impl(context):
    context.main_menu_link_page.test_oferta_zilei_button()


@when('user clicks on the Genius deals button')
def step_impl(context):
    context.main_menu_link_page.click_genius_deals_button()


@then('user is redirected to the Genius deals page')
def step_impl(context):
    context.main_menu_link_page.test_genius_deals_button()


@when('user clicks on the Genius button')
def step_impl(context):
    context.main_menu_link_page.click_genius_button()


@then('user is redirected to the Genius program page')
def step_impl(context):
    context.main_menu_link_page.test_genius_button()


@when('user clicks on the "Cardul cu idei" button')
def step_impl(context):
    context.main_menu_link_page.click_card_idei_button()


@then('user is redirected to the details page about "Cardul cu idei" program')
def step_impl(context):
    context.main_menu_link_page.test_card_idei_button()


@when('user clicks on the "Rabla" button')
def step_impl(context):
    context.main_menu_link_page.click_rabla_button()


@then('user is redirected to the details page about Rabla" program')
def step_impl(context):
    context.main_menu_link_page.test_rabla_button()


@when('user clicks on the "Oferte eMag" button')
def step_impl(context):
    context.main_menu_link_page.click_oferte_emag_button()


@then('user is redirected to the details page about "Oferte eMag" program')
def step_impl(context):
    context.main_menu_link_page.test_oferte_emag_button()

