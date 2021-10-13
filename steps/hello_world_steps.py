from behave import given, when, then

@given(u'there is a hello world')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given there is a hello world')


@when(u'I say hi')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I say hi')


@then(u'I get "Hello World" message')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I get "Hello World" message')
