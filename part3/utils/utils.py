from selenium import webdriver
from elementium.drivers.se import SeElements
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


# browser general options should be set at base.py
def setup_browser(context):
    if 'browser' in context.config.userdata.keys():
        browser = context.config.userdata.get('browser')
        if browser is None:
            context.browser = SeElements(webdriver.Chrome())
        elif browser == "chrome":
            context.browser = SeElements(webdriver.Chrome())
        elif browser == "chrome_h":
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("headless")
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--allow-running-insecure-content')
            chrome_options.add_argument('--ignore-certificate-errors')
            chrome_options.add_argument("--window-size=1920,1200")

            capabilities = DesiredCapabilities.CHROME.copy()
            capabilities['acceptSslCerts'] = True
            capabilities['acceptInsecureCerts'] = True

            context.browser = SeElements(webdriver.Chrome(chrome_options=chrome_options, desired_capabilities=capabilities))
    else:
        print("browser var does not exist",
              "Please configure a browser var within: userconfig.json - " +
              "behave.ini or using -D flag")
    return context.browser


def clean_browser(context):
    try:
        context.browser.browser.quit()
        context.browser = None
    except Exception as e:
        print(str(e))
