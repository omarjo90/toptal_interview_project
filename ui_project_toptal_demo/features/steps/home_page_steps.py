from behave import step
import time


# This step calls a method that redirects the
# webdriver to the homepage of the application
@step('I am on the home page')
def step_impl(context):
    context.home_page.go_to_home_page()


# This was implemented just for readability
@step('I click on sort button')
def step_impl(context):
    pass


# This step calls a method that selects
# the sort option: Z to A
@step('select the option Z to A')
def step_impl(context):
    context.home_page.select_z_to_a_option()


# This steps checks that the sort option Z to A
# displays the text of the first element displayed
# after sort was applied
@step('I noticed that item list is sorted')
def step_impl(context):
    assert context.home_page.check_z_to_a_sort_works() == 'Test.allTheThings() T-Shirt (Red)'


# This step call a method that clicks
# the left main menu of the page
@step('I click on the left principal menu')
def step_impl(context):
    context.home_page.click_menu_button()


# This step call a method to click the logout button
@step('click on Logout button')
def step_impl(context):
    context.home_page.click_logout_button()


# This step calls a method to check if an expected
# web element is displayed in UI
@step('Login page is displayed')
def step_impl(context):
    context.base_page.check_web_element_displayed(context.login_page.username_xpath)


# This steps calls a method to select the sort option low to high in UI
@step('select the option low to high')
def step_impl(context):
    context.home_page.select_low_to_high_option()


# This step calls a method to check if an expected sort
# option was correctly applied
@step('I noticed that item list is sorted low to high')
def step_impl(context):
    assert context.home_page.check_low_to_high_sort_works() == 'Sauce Labs Onesie'


# This steps calls a method to select the sort option high to low in UI
@step('select the option high to low')
def step_impl(context):
    context.home_page.select_high_to_low_option()


# This step calls a method to check if an expected sort
# option was correctly applied
@step('I noticed that item list is sorted high to low')
def step_impl(context):
    assert context.home_page.check_high_to_low_sort_works() == 'Sauce Labs Fleece Jacket'


