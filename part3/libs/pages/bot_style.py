import sys
sys.path.insert(0,"")
import hamcrest
from utils import exceptions_handler


def click(browser, selector):
    global se
    try:
        se = browser.xpath(selector["xpath"], wait=True)
    except (exceptions_handler.wrapping_exceptions()):
        try:
            se = browser.find(selector["css"], wait=True)
        except (exceptions_handler.wrapping_exceptions()) as e:
            return exceptions_handler.get_error_details(sys.exc_info(), e)
    try:
        hamcrest.assert_that(str(se), hamcrest.is_not("SeElements([])"))
        se.click()
    except (exceptions_handler.wrapping_exceptions()) as e:
        return exceptions_handler.get_error_details(sys.exc_info(), e)


def write(browser, selector, text):
    global se
    try:
        se = browser.xpath(selector["xpath"], wait=True)
    except (exceptions_handler.wrapping_exceptions()):

        for locator in selector:
            try:
                se = browser.find(selector[locator], wait=True)
            except (exceptions_handler.wrapping_exceptions()):
                continue
    try:
        hamcrest.assert_that(str(se), hamcrest.is_not("SeElements([])"))
        se.clear()
        se.write(text)
    except (exceptions_handler.wrapping_exceptions()) as e:
        return exceptions_handler.get_error_details(sys.exc_info(), e)


def search(browser, search_textbox, search_button, text):
    try:
        write(browser,search_textbox, text)
        click(browser,search_button)
    except (exceptions_handler.wrapping_exceptions()) as e:
        return exceptions_handler.get_error_details(sys.exc_info(), e)


def check_text(browser, selector, text):
    global se
    try:
        se = browser.xpath(selector["xpath"].format(text), wait=True)
    except (exceptions_handler.wrapping_exceptions()):

        for locator in selector:
            try:
                se = browser.find(selector[locator].format(text), wait=True)
            except (exceptions_handler.wrapping_exceptions()):
                continue
    try:
        hamcrest.assert_that(str(se), hamcrest.is_not("SeElements([])"))
        return se.text()
    except (exceptions_handler.wrapping_exceptions()) as e:
        return exceptions_handler.get_error_details(sys.exc_info(), e)
