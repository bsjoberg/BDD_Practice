from behave import given, when, then

import hello_world


@given(u'I have an application')
def step_impl(context):
    pass


@when(u'I say hi')
def step_impl(context):
    context.result = hello_world.sayhi()


@then(u'I hear "{expected_result}"')
def step_impl(context, expected_result):
    assert expected_result == context.result, 'Expect {}, got {}'.format(expected_result, context.result)
