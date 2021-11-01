from django.test import LiveServerTestCase
from behave import given, when, then
import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class NewVisitorTest(LiveServerTestCase):

    @given(u'I have django running')
    def step_impl(self):
        self.result = self.browser

    @given(u'I goto the to-do website')
    def step_impl(self):
        self.result = self.browser
        self.result.get('http://localhost:8000')
        assert str(self.result.title).__contains__('To-Do')
        header_text = self.result.find_element(By.TAG_NAME, 'h1').text
        assert str(header_text).__contains__('To-Do')

    @when(u'I go to the website')
    def step_impl(self):
        self.result.get('http://localhost:8000')

    @when(u'I add an item')
    def step_impl(self):
        # She is invited to enter a to-do item straight away
        inputbox = self.result.find_element(By.ID, 'id_new_item')
        assert inputbox.get_attribute('placeholder') == 'Enter a to-do item'

        # She types "Buy peacock feathers" into a text box (Edith's hobby
        # is tying fly-fishing lures)
        inputbox.send_keys('Buy peacock feathers')

        # When she hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list table
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

    @then(u'I see "{expected_result}" in the title')
    def step_impl(self, expected_result):
        assert expected_result in self.result.title, f"Expected {expected_result} but got {self.result.title}"

    @then(u'I see the item on my to-do list')
    def step_impl(self):
        table = self.result.find_element(By.ID, 'id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        found = False
        for i in range(len(rows)):
            if rows[i].text == '1: Buy peacock feathers':
                found = True
                break
        assert found
