from hamcrest import assert_that,equal_to
from selenium.webdriver.common.by import By
from SearchPage import SearchPage

@given('I navigate to the google page')
def step_impl(context):
    global searchPage
    searchPage = SearchPage(context)
    context.browser.get("https://google.com")
    assert_that(context.browser.title, equal_to("Google"))

@step('I search for "{search_term}"')
def step_impl(context, search_term):
    searchPage.searchTerm(search_term)

@step('I see a search result "{search_result}"')
def step_impl(context, search_result):
    text = searchPage.getElementMatchingText(search_result).text
    assert_that(text, equal_to(search_result))
