#!/bin/bash

virtualenv --python=/usr/local/bin/python3.7 venv
export CHROME_DRIVER_PATH='/Users/omar.guzman/PycharmProjects/UDR_UI/features/chromedriver'
source ./venv/bin/activate && pip install behave selenium allure-behave && behave -f allure_behave.formatter:AllureFormatter -o ./reports ./features

