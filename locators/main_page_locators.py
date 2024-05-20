import os

from page.base_page import WebPage
from page.elements import WebElement


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://manjaro.org/'

        super().__init__(web_driver, url)

    # Main search field
    # search = WebElement(id='header-search')
    # search_run_button = WebElement(xpath='//button[@type="submit"]')
    # Header locators
    header_menu_merchandise = WebElement(xpath='(//*[@id="desktop-menu"]//a)[1]')
    header_menu_hardware = WebElement(xpath='(//*[@id="desktop-menu"]//a)[2]')
    header_menu_contact = WebElement(xpath='(//*[@id="desktop-menu"]//a)[3]')
    header_menu_download = WebElement(xpath='(//*[@id="desktop-menu"]//a)[4]')
    header_menu_project = WebElement(xpath='(//*[@id="left-menu"]//button)[1]')
    header_menu_explore = WebElement(xpath='(//*[@id="left-menu"]//button)[2]')
    header_menu_learn = WebElement(xpath='(//*[@id="left-menu"]//button)[3]')
    header_menu_supporters = WebElement(xpath='(//*[@id="left-menu"]//button)[4]')

    header_locators = [
        header_menu_merchandise, header_menu_hardware, header_menu_contact,
        header_menu_download, header_menu_project, header_menu_explore,
        header_menu_learn, header_menu_supporters
    ]

    # Footer locators
    footer_menu_privacy_policy = WebElement(xpath='//*[@aria-label="Privacy Policy"]')
    footer_menu_terms_of_use = WebElement(xpath='//*[@aria-label="Terms of use"]')
    footer_menu_imprint = WebElement(xpath='//*[@aria-label="Imprint"]')
    footer_menu_facebook = WebElement(xpath='//*[@aria-label="Facebook"]')
    footer_menu_youtube = WebElement(xpath='//*[@aria-label="Youtube"]')
    footer_menu_twitter = WebElement(xpath='//*[@aria-label="Twitter"]')
    footer_menu_code_of_conduct = WebElement(xpath='//*[@aria-label="Code of Conduct"]')
    footer_menu_source_code = WebElement(xpath='//*[@aria-label="Source Code"]')
    footer_menu_sending_pr = WebElement(xpath='//*[@aria-label="Sending a PR"]')
    footer_menu_development = WebElement(xpath='//*[@aria-label="Development"]')
    footer_menu_packages = WebElement(xpath='//*[@aria-label="Packages"]')
    footer_menu_security = WebElement(xpath='//*[@aria-label="Security"]')
    footer_menu_general = WebElement(xpath='//*[@aria-label="General"]')
    footer_menu_testing = WebElement(xpath='//*[@aria-label="Testing"]')
    footer_menu_mirrors = WebElement(xpath='//*[@aria-label="Mirrors"]')
    footer_menu_log_in = WebElement(xpath='//*[@aria-label="Log in"]')

    footer_locators = [
        footer_menu_privacy_policy, footer_menu_terms_of_use, footer_menu_imprint,
        footer_menu_facebook, footer_menu_youtube, footer_menu_twitter, footer_menu_code_of_conduct,
        footer_menu_source_code, footer_menu_sending_pr, footer_menu_development,
        footer_menu_packages, footer_menu_security, footer_menu_general, footer_menu_testing,
        footer_menu_mirrors, footer_menu_log_in
    ]
