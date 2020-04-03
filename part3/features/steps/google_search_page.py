import sys
from hamcrest import assert_that, equal_to, is_not, is_
from selenium.webdriver.common.by import By
from behave import given, when, then, step

sys.path.append('../libs')
from libs.pages import *

@step(u'I search for "{search_term}"')
def step_i_search_for(context, search_term):
    context.page = PageBuilder("GoogleSearch")(context.browser)
    assert_that(context.page.search(search_term), is_not("Error when trying to search"))


@step('I see "{search_result}"')
def step_i_check_a_result(context, search_result):
    context.page = PageBuilder("GoogleSearch")(context.browser)
    assert_that(context.page.check_text_result(search_result), is_(equal_to(search_result)))
