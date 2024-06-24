import allure
import pytest_check as check

from locators.repository_page_locators import MainPage


@allure.story('Test repository page')
@allure.feature('Test checkboxes')
def test_checkbox(web_browser):
    """This test checking checkbox FTP"""

    page = MainPage(web_browser)

    ftp = page.checkbox_ftp
    http = page.checkbox_http
    https = page.checkbox_https

    protocol_field = page.column_protocols

    check.is_true()
