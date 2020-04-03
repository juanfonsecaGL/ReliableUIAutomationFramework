import sys, os
import pages.bot_style as bot

sys.path.insert(0, "")
from . import base
import libs.locators.google_search_locators as google_search_locators
from utils import exceptions_handler


class GoogleSearchPage(base.BasePage):
    def __init__(self, browser):
        super(GoogleSearchPage, self).__init__(browser)
        self.GSLocators = google_search_locators.GoogleSearchLocators

    def search(self, text):
        try:
            bot.search(self.browser, self.GSLocators.search_textbox, self.GSLocators.search_button, text)
        except (exceptions_handler.wrapping_exceptions()) as e:
            exceptions_handler.get_error_details(sys.exc_info(), e)
            return 'Error when trying to search'

    def check_text_result(self, text):
        try:
            return bot.check_text(self.browser, self.GSLocators.search_result, text)
        except (exceptions_handler.wrapping_exceptions()) as e:
            exceptions_handler.get_error_details(sys.exc_info(), e)
            return 'Error when trying to get the result text'
