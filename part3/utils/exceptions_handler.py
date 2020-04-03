import os
import selenium.common.exceptions
import elementium.elements, elementium.exc
import urllib.error


def get_error_details(exc_info, e):
    exc_type, exc_obj, exc_tb = exc_info
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    print(f"File: {str(fname)}\nLine number: {str(exc_tb.tb_lineno)}")
    error = "Selector not found" if str(e) == "return elements.until(lambda e: len(e) > 0, ttl=ttl)" else str(e)
    print(f"Something happened: {str(error)}\n")


def wrapping_exceptions():
    return selenium.common.exceptions.WebDriverException, AssertionError, selenium.common.exceptions.NoSuchElementException, \
           elementium.elements.TimeOutError, \
            TypeError, elementium.exc.TimeOutError, selenium.common.exceptions.UnexpectedTagNameException, AttributeError,  \
           selenium.common.exceptions.InvalidSelectorException, urllib.error.URLError
