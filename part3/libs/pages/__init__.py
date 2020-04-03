__author__ = 'dsolis'
"""
This class will handle all class pages within libs.pages
"""
# imports are not used until the return eval calls them
import google_search_page as GoogleSearchPage

class PageBuilder(object):
    """
    It will return the given class as  an object
    """
    def __new__(cls, page_name):
        try:
            return eval(page_name + 'Page.'+ page_name + 'Page')
        except NameError:
            print('Unable to find ' + page_name + 'Page' + '. Try adding the'
                  ' class to the pages __init__, verify the class'
                  ' exist within the libs.pages module, and double check the '
                  'class spelling ')
