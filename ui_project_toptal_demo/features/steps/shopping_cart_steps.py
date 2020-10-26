from behave import step


@step('I click on the first add to cart button')
def step_impl(context):
    context.home_page.click_first_add_to_cart_button()


@step('I click on the shopping cart')
def step_impl(context):
    context.home_page.click_shopping_cart()


@step('I noticed that one package was added')
def step_impl(context):
    context.base_page.check_web_element_displayed(context.shopping_cart_page.cart_quantity)


@step('I am on shopping cart page')
def step_impl(context):
    context.base_page.check_web_element_displayed(context.shopping_cart_page.remove_button)


@step('I click on remove button')
def step_impl(context):
    context.shopping_cart_page.remove_item_from_shopping_cart()


@step('I noticed that the item was removed')
def step_impl(context):
    assert context.shopping_cart_page.check_item_was_removed()


@step('I click on the second item to add to cart button')
def step_impl(context):
    context.home_page.click_second_add_to_cart_button()


@step('I noticed that second package was added')
def step_impl(context):
    assert context.shopping_cart_page.check_second_item_added()


@step('I go to shopping cart page')
def step_impl(context):
    context.home_page.go_to_shopping_cart_page()


@step('I click on checkout button')
def step_impl(context):
    context.shopping_cart_page.click_checkout_button()


@step('I noticed 3 fields displayed')
def step_impl(context):
    assert context.shopping_cart_page.check_labels_to_checkout_displays()


@step('I filled then up')
def step_impl(context):
    context.shopping_cart_page.fill_checkout_information()


@step('I click on continue button')
def step_impl(context):
    context.shopping_cart_page.click_continue_button_to_checkout()


@step('I overview the order')
def step_impl(context):
    assert context.shopping_cart_page.overview_order()


@step('I click on finish button')
def step_impl(context):
    context.shopping_cart_page.click_finish_button()


@step('I noticed that order was dispatched')
def step_impl(context):
    assert context.shopping_cart_page.check_order_dispatched()
