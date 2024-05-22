import pytest
import allure
import pytest_check as check
from locators.main_page_locators import MainPage


def test_headers(web_browser):
    """Этот тест проверяет хедер главной страницы"""

    page = MainPage(web_browser)

    header_locators = [
        page.header_menu_merchandise, page.header_menu_hardware, page.header_menu_contact,
        page.header_menu_download, page.header_menu_project, page.header_menu_explore,
        page.header_menu_learn, page.header_menu_supporters
    ]
    # check.equal(page.search_run_button.get_text(), 'Дом43ены', 'Тест локатора не равен ожидаймому результату')
    # check.is_true(page.search_run_button.is_visible())
    check.is_true(page.head_link_btn_group.is_clickable())
    check.is_true(page.foot_link_btn_group.is_clickable())

    # for elements in header_locators:
    #     # with allure.step(f'Checking the element "" for clickability'):
    #     #     check.is_true(elements)
    #
    #     with allure.step(f'Checking element "" for display'):
    #         check.is_true(elements.is_clickable())

