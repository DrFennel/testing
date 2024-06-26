import allure
import pytest_check as check
import time
from selenium.webdriver.support.ui import Select
from locators.repository_page_locators import MainPage
from selenium import webdriver
from selenium.webdriver.common.by import By


@allure.story('Test repository page')
@allure.feature('Test checkboxes')
def test_checkbox(web_browser):
    """This test checking checkbox"""

    page = MainPage(web_browser)

    checkboxes = [
        (page.checkbox_http, page.checkbox_http_label, 'HTTP'),
        (page.checkbox_https, page.checkbox_https_label, 'HTTPS'),
        (page.checkbox_ftp, page.checkbox_ftp_label, 'FTP')
    ]

    page.scroll_up()

    for checkbox, checkbox_label, checkbox_text in checkboxes:

        with allure.step(f'Checking element "{checkbox_text}" for presented'):
            check.is_true(checkbox_label.is_presented(), f'Checkbox {checkbox_text} is not presented')

        with allure.step(f'Checking the text of the element "{checkbox_text}"'):
            check.is_true(checkbox_label.is_visible(), f'Checkbox text {checkbox_text} is not displayed')

        with allure.step(f'Checking element "{checkbox_text}" for clickability'):
            check.is_true(checkbox_label.is_clickable(), f'Checkbox {checkbox_text} is not clickable')

        with allure.step(f'Checking that the element "{checkbox_text}" is selected'):
            if checkbox.is_selected() is True:
                checkbox_label.click()
                time.sleep(1)
            check.is_false(checkbox.is_selected(), f'Checkbox {checkbox_text} is not selected')


@allure.story('Test repository page')
@allure.feature('Test dropdown menu')
def test_dropdown():
    """This test checking dropdown menu"""

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://repo.manjaro.org/")

    dropdown_countries = driver.find_element(By.XPATH, '//*[@id="country-filter"]')
    text = 'netherlands'

    with allure.step(f'Checking element "countries" menu for selectability'):
        select = Select(dropdown_countries)
        select.select_by_value(text)
