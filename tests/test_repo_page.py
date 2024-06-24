import allure
import pytest_check as check

from locators.repository_page_locators import MainPage


@allure.story('Test repository page')
@allure.feature('Test checkboxes')
def test_checkbox(web_browser):
    """This test checking checkbox"""

    page = MainPage(web_browser)

    checkboxes = [
        (page.checkbox_http, page.checkbox_http_label, 'HTTP'),
        (page.checkbox_https, page.checkbox_https_label_label, 'HTTPS'),
        (page.checkbox_ftp, page.checkbox_ftp_label, 'FTP')
    ]

    protocol_field = page.column_protocols




