#!/bin/bash
python -m pytest --alluredir /home/fennel/PycharmProjects/testing/allure_results
pytest -v -s /home/fennel/PycharmProjects/testing/tests/
