from behave import given, when, then
from selenium import webdriver


def after_all(context):
    print("after")


@given(u'I have django running')
def step_impl(context):
    context.result = context.browser


@when(u'I go to the website')
def step_impl(context):
    context.result.get('http://localhost:8000')


@then(u'I see "{expected_result}" in the title')
def step_impl(context, expected_result):
    assert expected_result in context.result.title, f"Expected {expected_result} but got {context.result.title}"
