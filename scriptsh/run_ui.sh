#!/bin/bash
python -m pytest ../tests --alluredir /home/fennel/PycharmProjects/testing/allure_results
pytest -v -s /home/fennel/PycharmProjects/testing/tests/
