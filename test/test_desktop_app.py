from selenium.webdriver.common.by import By

from data import config
from resources import helper


def test_verify_the_download_links(start_driver):
    start_driver.get(config.URL)
    helper.click_on_element(start_driver, config.ELEMENT_XPATH)
    links = start_driver.find_elements(By.TAG_NAME, "a")
    linux_link_list = helper.create_list_for_linux_dist_download_links(links, config.regex_pattern)
    helper.verify_all_linux_links(linux_link_list)
