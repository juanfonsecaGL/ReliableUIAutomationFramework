from hamcrest import assert_that, equal_to, is_


@step(u'I navigate to google page')
def step_impl(context):
    context.login_url=context.config.userdata.get('url')
    context.browser.get(context.login_url)
    assert_that(context.browser.browser.title, is_(equal_to("Google")))
