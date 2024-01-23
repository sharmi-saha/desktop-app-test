import logging
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from pytest import fixture


@fixture(scope='session')
def start_driver():
    logging.info("starting firefox headless driver")
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options, executable_path='geckodriver.exe')
    yield driver
    driver.quit()
