class GoogleSearchLocators():
    search_button = {
        "css": "ul[role='listbox'] > li:nth-of-type(1)  div[role='option']  span",
        "xpath": "//*//ul[@role='listbox']/li[1]//div[@role='option']//span]"
    }

    search_textbox = {
        "css": "[maxlength]",
        "xpath": "//*/input[@role='combobox']"
    }

    search_result ={
        "xpath": "//*/h3[contains(.,'{}')]"
    }
