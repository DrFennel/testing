#!/bin/bash
#python -m pytest -v -s ../tests --alluredir ../allure_results

# Получаем текущую директорию скрипта
SCRIPT_DIR=$(dirname "$0")
pwd

# Определяем путь к тестовому файлу относительно директории со скриптом
TEST_FILE="$SCRIPT_DIR/../tests/"

# Определяем путь к директории с отчетами относительно директории со скриптом
REPORT_DIR="$SCRIPT_DIR/../allure_results"

# Запускаем pytest с использованием относительного пути к файлу test_main_page.py и директории с отчетами
pytest -v -s "$TEST_FILE" --alluredir="$REPORT_DIR"