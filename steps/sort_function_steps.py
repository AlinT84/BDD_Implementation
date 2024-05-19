from behave import *


# @given("user is on the Main Page")
# def step_impl(context):
#     context.sort_function_page.go_to_main_page()


@given('user searches the product')
def step_impl(context):
    context.sort_function_page.search_product()


@when('user clicks on the "Ordoneaza" drop-down menu')
def step_impl(context):
    context.sort_function_page.click_sort_menu()


@when('user clicks on the "Pret crescator" button')
def step_impl(context):
    context.sort_function_page.select_ascending_option()


@then('results are sorted in the ascending price order')
def step_impl(context):
    context.sort_function_page.assert_ascending_order()


@when('user clicks on the "Pret descrescator" button')
def step_impl(context):
    context.sort_function_page.select_descending_option()


@then('results are sorted in the descending price order')
def step_impl(context):
    context.sort_function_page.assert_descending_order()


@when('user clicks on the "Nr. review-uri" button')
def step_impl(context):
    context.sort_function_page.select_review_order()


@then('results are sorted in ascending order by the number of reviews')
def step_impl(context):
    context.sort_function_page.assert_by_review_order()
