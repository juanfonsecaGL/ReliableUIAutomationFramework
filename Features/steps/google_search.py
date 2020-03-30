from hamcrest import assert_that,equal_to
from selenium.webdriver.common.by import By


@step('I navigate to the google page')
def step_impl(context):
    context.browser.get("https://google.com")
    assert_that(context.browser.title, equal_to("Google"))


@step('I search for "{search_term}"')
def step_impl(context, search_term):
    context.browser.xpath("//*/input[@role='combobox']").write(search_term)
    context.browser.xpath("(//*/input[@name='btnK'])[2]").click()


@step('I see a search result "{search_result}"')
def step_impl(context, search_result):
    element = context.browser.xpath("//*/h3[contains(.,'{}')]".format(search_result))
    assert_that(element.text(), equal_to(search_result))