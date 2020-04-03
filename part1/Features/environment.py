from selenium import webdriver

def before_all(context):
    context.browser = webdriver.Chrome() #have set chromedriver in your PATH
    context.browser.set_page_load_timeout(20)
    context.browser.implicitly_wait(20)
    context.browser.maximize_window()

def after_all(context):
    context.browser.quit()
