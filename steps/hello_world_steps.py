from behave import given, when, then

import hello_world


@given(u'there is a hello world')
def step_impl(context):
    pass


@when(u'I say hi')
def step_impl(context):
    context.result = hello_world.sayhi()


@then(u'I get "Hello World" message')
def step_impl(context):
    assert context.result == "Hello World"
