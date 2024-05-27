import os

from page.base_page import WebPage
from page.elements import WebElement
from page.elements import ManyWebElements


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            # url = os.getenv("MAIN_URL") or 'https://hoster.by/'
            url = os.getenv("MAIN_URL") or 'https://manjaro.org/'

        super().__init__(web_driver, url)

    # Main search field
    search_field = WebElement(id='search-query')

    # Header locators
    btn_logo = WebElement(xpath='(//*[@aria-label="Home"])[1]')
    header_menu_merchandise = WebElement(xpath='(//*[@id="desktop-menu"]//a)[1]')
    header_menu_hardware = WebElement(xpath='((//*[@id="desktop-menu"]//ul)[1]//a)[2]')
    header_menu_contact = WebElement(xpath='(//*[@id="desktop-menu"]//a)[3]')
    header_menu_download = WebElement(xpath='(//*[@id="desktop-menu"]//a)[4]')
    header_menu_project = WebElement(xpath='(//*[@id="left-menu"]//button)[1]')
    header_menu_explore = WebElement(xpath='(//*[@id="left-menu"]//button)[2]')
    header_menu_learn = WebElement(xpath='(//*[@id="left-menu"]//button)[3]')
    header_menu_supporters = WebElement(xpath='(//*[@id="left-menu"]//button)[4]')
    header_donate = WebElement(xpath='//a[@id="donate-btn"]')
    # Search
    header_search_field = WebElement(xpath='(//*[@name="query"])[1]')
    header_submit_btn = WebElement(xpath='(//*[@type="submit"])[1]')
    # Links menu
    head_link_btn_group = ManyWebElements(xpath='((//*[@id="desktop-menu"]//ul)[1]//a)')
    # Dropdown menu
    head_dd_btn_group = ManyWebElements(xpath='(//*[@id="left-menu"]//button)')

    # Body locators
    body_get_manjaro_btn = ManyWebElements(xpath='(//*[@id="download-btn"])')
    # Text
    body_main_title = WebElement(xpath='//main//h1')
    body_group_block_title_text = ManyWebElements(xpath='//main//h3')
    body_group_title_text = ManyWebElements(xpath='//main//h2')
    body_group_text = ManyWebElements(xpath='//main//p')

    # Right pointed text
    body_right_text = ManyWebElements(xpath='//main//li')
    # Scroll buttons
    body_scroll_desktops_btn = WebElement(xpath='//a[@href="#desktops"]')
    body_scroll_software_btn = WebElement(xpath='//a[@href="#software"]')
    body_scroll_branches_btn = WebElement(xpath='//a[@href="#branches"]')
    body_scroll_merch_btn = WebElement(xpath='//a[@href="#merch"]')
    body_scroll_blog_btn = WebElement(xpath='//a[@href="#blog"]')

    body_group_scroll_btn = ManyWebElements(xpath='//*[@aria-label="scroll"]')

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

    # Footer links locators without "log in"
    foot_link_btn_group = ManyWebElements(xpath='//*[@id="link-grid"]//li')

    # Footer login link
    footer_menu_log_in = WebElement(xpath='//*[@aria-label="Log in"]')

    # Footer title columns
    foot_title_columns = ManyWebElements(xpath='//footer//h4')
