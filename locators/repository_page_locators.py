import os

from page.base_page import WebPage
from page.elements import WebElement
from page.elements import ManyWebElements


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://manjaro.org/'

        super().__init__(web_driver, url)

    # Filters
    checkbox_http = WebElement(xpath='//*[@id="http-filter"]')
    checkbox_http_label = WebElement(xpath='//*[@for="http-filter"]')
    checkbox_https = WebElement(xpath='//*[@id="https-filter"]')
    checkbox_https_label = WebElement(xpath='//*[@for="https-filter"]')
    checkbox_ftp = WebElement(xpath='//*[@id="ftp-filter"]')
    checkbox_ftp_label = WebElement(xpath='//*[@for="ftp-filter"]')

    drop_countries = WebElement(xpath='//*[@value="netherlands"]')
    drop_states = WebElement(xpath='//*[@value="part"]')

    # Rows
    column_country = ManyWebElements(xpath='//*[@aria-live="polite"]/*[*]/*[2]')
    column_protocols = ManyWebElements(xpath='//*[@aria-live="polite"]/*[*]/*[3]')
    column_stable = ManyWebElements(xpath='(//*[@role="row"])[*]/*[5]')
    column_testing = ManyWebElements(xpath='(//*[@role="row"])[*]/*[6]')
    column_unstable = ManyWebElements(xpath='(//*[@role="row"])[*]/*[6]')
