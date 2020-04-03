"""
This is the base class where basic browser settings are set up
"""


class BasePage(object):
    def __init__(self, browser):
        self.browser = browser
        #for example
        #self.browser.browser.set_page_load_timeout(10)
