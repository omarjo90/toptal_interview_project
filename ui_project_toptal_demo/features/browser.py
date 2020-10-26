from selenium import webdriver
import os


# This class is created in order to provide webdriver methods to the pages in the project
class Browser(object):
    chrome_driver = os.environ['CHROME_DRIVER_PATH']
    driver = webdriver.Chrome(chrome_driver)
    driver.implicitly_wait(15)
    driver.maximize_window()

    def close(self):
        self.driver.close()
