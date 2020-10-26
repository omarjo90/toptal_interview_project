from behave import step
import configparser

config = configparser.ConfigParser()
config.read('features/config.ini')
username = config['Credentials']['user']
password = config['Credentials']['pass']


# This step calls the webdriver get method in order to open
# the web browser where the automation test will be executed
@step('the swag labs page is displayed')
def step_impl(context):
    context.browser.driver.get('https://www.saucedemo.com/index.html')


# This step call a login method that performs the input of
# the username and password in UI and clicking in login button
@step('I write the username and password')
def step_impl(context):
    context.login_page.login_to_swag_labs(username, password)


# This step is only for readability of the end user
@step('I click on login Button')
def step_impl(context):
    pass


# This step check is a web element is displayed for checking that
# user logs in successfully
@step('I will see the home page of swag labs displayed')
def step_impl(context):
    assert context.base_page.check_web_element_displayed(context.home_page.sort_container)
