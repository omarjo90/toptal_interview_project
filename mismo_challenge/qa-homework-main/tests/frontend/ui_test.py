import json
import time
import pytest
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


@pytest.fixture(scope="class")
def driver_init(request):
    driver = webdriver.Chrome(r'C:\Users\omar\Downloads\chromedriver_win32\chromedriver.exe')
    request.cls.driver = driver
    driver.maximize_window()
    driver.get('http://localhost:3000/')
    yield
    driver.quit()


@pytest.mark.usefixtures('driver_init')
class TestSpreadsheet():
    def test_add_numbers_to_cell(self):
        cell_b1 = self.driver.find_element_by_xpath('(//span[@class="Cell__Span-htg9i1-0 hOGgfP"])[2]')
        cell_b1.click()
        fx_field = self.driver.find_element(By.XPATH, "(//input[@class='sc-AxjAm emkAjW Formula___StyledCellValueInput-sc-1613qao-2 dyVqsa'])")
        fx_field.click()
        length = len(fx_field.get_attribute('value'))
        if length > 0:
            fx_field.send_keys(length * Keys.BACKSPACE)
            fx_field.send_keys(Keys.ENTER)
            self.driver.refresh()
            cell_b1 = self.driver.find_element_by_xpath('(//span[@class="Cell__Span-htg9i1-0 hOGgfP"])[2]')
            actionChains = ActionChains(self.driver)
            actionChains.double_click(cell_b1).perform()
            input_field = self.driver.find_element_by_xpath("(//input[@class='sc-AxjAm emkAjW'])")
            input_field.send_keys(123)
            input_field.send_keys(Keys.ENTER)
            cell_b1 = self.driver.find_element_by_xpath('(//span[@class="Cell__Span-htg9i1-0 hOGgfP"])[2]')
            expected_value = cell_b1.text
            assert expected_value == str(123)
        else:
            input_field = self.driver.find_element_by_xpath("(//input[@class='sc-AxjAm emkAjW'])")
            input_field.send_keys(789)
            input_field.send_keys(Keys.ENTER)
            cell_b1 = self.driver.find_element_by_xpath('(//span[@class="Cell__Span-htg9i1-0 hOGgfP"])[2]')
            expected_value = cell_b1.text
            assert expected_value == str(789)

    def test_sum_between_cells(self):
        cell_c1 = self.driver.find_element_by_xpath('(//span[@class="Cell__Span-htg9i1-0 hOGgfP"])[3]')
        cell_c1.click()
        fx_field = self.driver.find_element(By.XPATH,
                                            "(//input[@class='sc-AxjAm emkAjW Formula___StyledCellValueInput-sc-1613qao-2 dyVqsa'])")
        length = len(fx_field.get_attribute('value'))
        if length > 0:
            fx_field.click()
            fx_field.send_keys(length * Keys.BACKSPACE)
            fx_field.send_keys(Keys.ENTER)
            self.driver.refresh()
            cell_c1 = self.driver.find_element_by_xpath('(//span[@class="Cell__Span-htg9i1-0 hOGgfP"])[3]')
            actionChains = ActionChains(self.driver)
            actionChains.double_click(cell_c1).perform()
            input_field = self.driver.find_element_by_xpath("(//input[@class='sc-AxjAm emkAjW'])")
            input_field.send_keys(5)
            input_field.send_keys(Keys.ENTER)
        else:
            cell_c1 = self.driver.find_element_by_xpath('(//span[@class="Cell__Span-htg9i1-0 hOGgfP"])[3]')
            actionChains = ActionChains(self.driver)
            actionChains.double_click(cell_c1).perform()
            input_field = self.driver.find_element_by_xpath("(//input[@class='sc-AxjAm emkAjW'])")
            input_field.send_keys(5)
            input_field.send_keys(Keys.ENTER)

        cell_d1 = self.driver.find_element_by_xpath('(//span[@class="Cell__Span-htg9i1-0 hOGgfP"])[4]')
        cell_d1.click()
        fx_field = self.driver.find_element(By.XPATH,
                                            "(//input[@class='sc-AxjAm emkAjW Formula___StyledCellValueInput-sc-1613qao-2 dyVqsa'])")
        length = len(fx_field.get_attribute('value'))
        if length > 0:
            fx_field.click()
            fx_field.send_keys(length * Keys.BACKSPACE)
            fx_field.send_keys(Keys.ENTER)
            self.driver.refresh()
            cell_d1 = self.driver.find_element_by_xpath('(//span[@class="Cell__Span-htg9i1-0 hOGgfP"])[4]')
            actionChains = ActionChains(self.driver)
            actionChains.double_click(cell_d1).perform()
            input_field = self.driver.find_element_by_xpath("(//input[@class='sc-AxjAm emkAjW'])")
            input_field.send_keys(7)
            input_field.send_keys(Keys.ENTER)
        else:
            cell_d1 = self.driver.find_element_by_xpath('(//span[@class="Cell__Span-htg9i1-0 hOGgfP"])[4]')
            actionChains = ActionChains(self.driver)
            actionChains.double_click(cell_d1).perform()
            input_field = self.driver.find_element_by_xpath("(//input[@class='sc-AxjAm emkAjW'])")
            input_field.send_keys(7)
            input_field.send_keys(Keys.ENTER)

        cell_e1 = self.driver.find_element_by_xpath('(//span[@class="Cell__Span-htg9i1-0 hOGgfP"])[5]')
        cell_e1.click()
        fx_field = self.driver.find_element(By.XPATH,
                                            "(//input[@class='sc-AxjAm emkAjW Formula___StyledCellValueInput-sc-1613qao-2 dyVqsa'])")
        length = len(fx_field.get_attribute('value'))
        if length > 0:
            fx_field.click()
            fx_field.send_keys(length * Keys.BACKSPACE)
            fx_field.send_keys(Keys.ENTER)
            self.driver.refresh()
            cell_e1 = self.driver.find_element_by_xpath('(//span[@class="Cell__Span-htg9i1-0 hOGgfP"])[5]')
            actionChains = ActionChains(self.driver)
            actionChains.double_click(cell_e1).perform()
            input_field = self.driver.find_element_by_xpath("(//input[@class='sc-AxjAm emkAjW'])")
            input_field.send_keys('=C1+D1')
            input_field.send_keys(Keys.ENTER)
        else:
            cell_e1 = self.driver.find_element_by_xpath('(//span[@class="Cell__Span-htg9i1-0 hOGgfP"])[5]')
            actionChains = ActionChains(self.driver)
            actionChains.double_click(cell_e1).perform()
            input_field = self.driver.find_element_by_xpath("(//input[@class='sc-AxjAm emkAjW'])")
            input_field.send_keys('=C1+D1')
            input_field.send_keys(Keys.ENTER)

        self.driver.refresh()

        cell_e1 = self.driver.find_element_by_xpath('(//span[@class="Cell__Span-htg9i1-0 hOGgfP"])[5]')
        expected_result = cell_e1.text
        assert expected_result == str(12)

    def test_ent_to_end_(self):
        base_url = 'http://127.0.0.1:5000/api'
        payload = {
            'value': '=E1'
        }

        response = requests.put(f'{base_url}/cell/A_10/', json=payload)
        # print(json.dumps(response.json(), indent=4))
        assert response.status_code == 200
        assert response.json()[0].get('value') == '=E1'
        assert response.json()[0].get('computed') == 12

        cell_a10 = self.driver.find_element_by_xpath("(//span[@class='Cell__Span-htg9i1-0 hOGgfP'])[91]")
        expected_result = cell_a10.text
        assert expected_result == str(12)

