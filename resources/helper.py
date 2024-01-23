import re
import pytest
import requests
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
import logging


def click_on_element(driver, x_pth):
    try:
        element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, x_pth)))
        element.location_once_scrolled_into_view
        time.sleep(5)
        element.click()
    except Exception as e:
        logging.error(e)
        pytest.fail()


def create_list_for_linux_dist_download_links(links, regex):
    p = re.compile(regex)
    linux_distribution_download_link = []
    logging.info(f"Total links in the page, {len(links)}")
    logging.info("------- Below linux distribution links are available in Mega Desktop page ------")
    for i in links:
        url = i.get_attribute("href")
        if url is None:
            continue
        match = re.search(p, url)
        if match:
            logging.info(url)
            linux_distribution_download_link.append(url)
    linux_links = len(linux_distribution_download_link)
    logging.info(f"Total linux distribution download links, {linux_links}")
    return linux_distribution_download_link


def verify_all_linux_links(links):
    good_links = 0
    err_links = []
    se = requests.session()
    for i in links:
        resp = se.get(url=i)
        if resp.status_code == 200 or resp.status_code == 302:
            good_links += 1
        else:
            err_links.append(i)
            logging.info(f"broken link found, {i}")
    assert good_links == len(links),  "All links are not working properly. "
