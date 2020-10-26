from features.pages.base_page import BasePage



class LoginPage(BasePage):
    # LOCATORS
    username_field = 'user-name'
    password_field = 'password'
    login_button = 'login-button'
    username_xpath = "//input[@id='user-name']"

    # Methods that perform login page actions

    # This methods allows to log in a valid user to the application
    def login_to_swag_labs(self, username_, password_):
        username = self.driver.find_element_by_id(self.username_field)
        password = self.driver.find_element_by_id(self.password_field)
        log_in_button = self.driver.find_element_by_id(self.login_button)

        username.click()
        username.send_keys(username_)

        password.click()
        password.send_keys(password_)

        log_in_button.click()


