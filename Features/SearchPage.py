class SearchPage:

    context = None

    def __init__(self, context):
        self.context = context

    def searchTerm(self, search_term):
        self.context.browser.find_element_by_xpath("//*/input[@role='combobox']").send_keys(search_term)
        self.context.browser.find_element_by_xpath("(//*/input[@name='btnK'])[2]").click()

    def getElementMatchingText(self, search_result):
        return self.context.browser.find_element_by_xpath("//*/h3[contains(.,'{}')]".format(search_result))
