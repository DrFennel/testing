import allure
import pytest_check as check
from project.locators.main_page_locators import MainPage
from selenium.webdriver.common.keys import Keys


@allure.story('Test main page')
@allure.feature('Test header')
def test_headers(web_browser):
    """This test checking header main page"""

    page = MainPage(web_browser)

    header_locators = [
        (page.header_menu_merchandise, 'Merchandise'),
        (page.header_menu_hardware, 'Hardware'),
        (page.header_menu_contact, 'Contact'),
        (page.header_menu_download, 'Download'),
        (page.header_menu_project, 'Project'),
        (page.header_menu_explore, 'Explore'),
        (page.header_menu_learn, 'Learn'),
        (page.header_menu_supporters, 'Supporters'),
        (page.header_donate, 'Donate')
    ]

    for element, element_text in header_locators:
        with allure.step(f'Checking element "{element}" for visible'):
            check.is_true(element.is_visible())

        with allure.step(f'Checking element "{element}" for clickability'):
            check.is_true(element.is_clickable())

        with allure.step(f'Checking the text of the element "{element}"'):
            btn_text = element.get_text()
            check.equal(btn_text, element_text,
                        f'Locator text "{element_text}" is not equal to the expected result')


@allure.story('Test main page')
@allure.feature('Test find field')
def test_find_field(web_browser):
    """This test checking search main page"""

    page = MainPage(web_browser)

    with allure.step('Check visibility'):
        check.is_true(page.search_field.is_visible())

    with allure.step('Check clickability'):
        check.is_true(page.search_field.is_clickable())

    with allure.step('Check placeholder'):
        check.equal(page.search_field.get_attribute('placeholder'), 'Search..')

    with allure.step('Enter text'):
        text = 'arch'
        page.search_field.send_keys(text)
        page.search_field.send_keys(Keys.RETURN)


@allure.story('Test main page')
@allure.feature('Test footer')
def test_footer(web_browser):
    """This test checking footer main page"""

    page = MainPage(web_browser)

    header_locators = [
        (page.footer_menu_privacy_policy, 'Privacy Policy'),
        (page.footer_menu_terms_of_use, 'Terms Of Use'),
        (page.footer_menu_imprint, 'Imprint'),
        (page.footer_menu_facebook, 'Facebook'),
        (page.footer_menu_youtube, 'Youtube'),
        (page.footer_menu_twitter, 'Twitter'),
        (page.footer_menu_code_of_conduct, 'Code Of Conduct'),
        (page.footer_menu_source_code, 'Source Code'),
        (page.footer_menu_sending_pr, 'Sending A PR'),
        (page.footer_menu_development, 'Development'),
        (page.footer_menu_packages, 'Packages'),
        (page.footer_menu_security, 'Security'),
        (page.footer_menu_general, 'General'),
        (page.footer_menu_testing, 'Testing'),
        (page.footer_menu_mirrors, 'Mirrors'),
        (page.footer_menu_log_in, 'log in')
    ]

    for element, element_text in header_locators:
        with allure.step(f'Checking element "{element}" for visible'):
            check.is_true(element.is_visible())

        with allure.step(f'Checking element "{element}" for clickability'):
            check.is_true(element.is_clickable())

        with allure.step(f'Checking the text of the element "{element}"'):
            btn_text = element.get_text()
            check.equal(btn_text, element_text,
                        f'Locator text "{element_text}" is not equal to the expected result')


@allure.story('Test main page')
@allure.feature('Test navigation')
def test_navigation(web_browser):
    """This test checking navigation button main page"""

    page = MainPage(web_browser)

    scroll_locators = [
        (page.body_scroll_desktops_btn, 'https://manjaro.org/#desktops'),
        (page.body_scroll_software_btn, 'https://manjaro.org/#software'),
        (page.body_scroll_branches_btn, 'https://manjaro.org/#branches'),
        (page.body_scroll_merch_btn, 'https://manjaro.org/#merch'),
        (page.body_scroll_blog_btn, 'https://manjaro.org/#blog')
    ]

    for element, link in scroll_locators:
        with allure.step(f'Checking element "{element}" for visible'):
            check.is_true(element.is_visible())
        with allure.step(f'Checking element "{element}" for clickability'):
            check.is_true(element.is_clickable())
        with allure.step(f'Checking element "{element}" for working'):
            check.equal(element.get_attribute('href'), link)


@allure.story('Test main page')
@allure.feature('Test "GET MANJARO" button')
def test_get_manjaro(web_browser):
    """This test checking "Get Manjaro" button main page"""

    page = MainPage(web_browser)

    btn_get = page.body_get_manjaro_btn

    for element in btn_get:
        # with allure.step(f'Checking element "{element}" for visible'):
        #     check.is_true(element.is_enabled())
        # with allure.step(f'Checking element "{element}" for clickability'):
        #     check.is_true(element.is_clickable())
        with allure.step(f'Checking element "{element}" for working'):
            check.equal(element.get_attribute('href'), 'https://manjaro.org/download/')


# def test_test(web_browser):
#
#     page = MainPage(web_browser)
#
#     print(page.body_group_block_title_text.__getitem__(1).is_displayed())
#
#     check.equal(page.btn_logo.get_attribute('href'), 'https://manjaro.org/')
