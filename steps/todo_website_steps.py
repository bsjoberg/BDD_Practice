from unittest import TestCase

from behave import given, when, then
import time

from selenium.common.exceptions import WebDriverException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver

MAX_WAIT = 5
TO_DO_URL = 'http://localhost:8000'


def wait_for_row_in_list_table(self, row_text):
    start_time = time.time()
    while True:
        try:
            table = self.browser.find_element(By.ID, 'id_list_table')
            rows = table.find_elements_by_tag_name('tr')
            assert any(row_text in row.text for row in rows)
            return
        except (AssertionError, WebDriverException) as e:
            if time.time() - start_time > MAX_WAIT:
                raise e
            time.sleep(0.5)


@given(u'I have django running')
def step_impl(self):
    self.result = self.browser


@given(u'I goto the to-do website')
def step_impl(self):
    self.result = self.browser
    self.result.get(TO_DO_URL)
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
    inputbox.send_keys('Buy socks')

    # When she hits enter, the page updates, and now the page lists
    # "1: Buy peacock feathers" as an item in a to-do list table
    inputbox.send_keys(Keys.ENTER)
    wait_for_row_in_list_table(self, '1: Buy socks')


@when(u'someone else adds an item')
def step_impl(self):
    browser = self.result

    browser.execute_script('''window.open("http://localhost:8000", "_blank");''')
    browser.find_element(By.TAG_NAME, 'body').send_keys(Keys.CONTROL + Keys.TAB)
    window_after = browser.window_handles[1]
    browser.switch_to.window(window_after)

    inputbox = browser.find_element(By.ID, 'id_new_item')
    assert inputbox.get_attribute('placeholder') == 'Enter a to-do item'

    # She types "Buy peacock feathers" into a text box (Edith's hobby
    # is tying fly-fishing lures)
    inputbox.send_keys('Practice BDD')

    # When she hits enter, the page updates, and now the page lists
    # "1: Buy peacock feathers" as an item in a to-do list table
    inputbox.send_keys(Keys.ENTER)
    wait_for_row_in_list_table(self, '1: Practice BDD')

    browser.switch_to.window(browser.window_handles[0])


@then(u'I see "{expected_result}" in the title')
def step_impl(self, expected_result):
    assert expected_result in self.result.title, f"Expected {expected_result} but got {self.result.title}"


@then(u'I see the item on my to-do list')
def step_impl(self):
    table = self.result.find_element(By.ID, 'id_list_table')
    rows = table.find_elements_by_tag_name('tr')
    found = False
    for i in range(len(rows)):
        if rows[i].text == '1: Buy socks':
            found = True
            break
    assert found


@then(u'I don\'t see someone elses item')
def step_impl(self):
    table = self.result.find_element(By.ID, 'id_list_table')
    rows = table.find_elements_by_tag_name('tr')
    found = True
    for i in range(len(rows)):
        if rows[i].text == '2: Practice BDD':
            found = False
            break
    assert found
