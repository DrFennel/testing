import pytest
import allure
import pytest_check as check
from locators.main_page_locators import MainPage


def test_headers(web_browser):
    """Этот тест проверяет хедер главной страницы"""

    page = MainPage(web_browser)

    # check.equal(page.search_run_button.get_text(), 'Дом43ены', 'Тест локатора не равен ожидаймому результату')
    # check.is_true(page.search_run_button.is_visible())

    for elements in page.header_locators:
        # with allure.step(f'Checking the element "" for clickability'):
        #     check.is_true(elements)

        with allure.step(f'Checking element "" for display'):
            check.is_true(elements.is_visible())

        # with allure.step(f'Checking element text ""'):
        #     check.equal(elements.text, elements_text)
