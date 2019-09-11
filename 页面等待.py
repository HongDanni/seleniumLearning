# -*-coding;utf8-*-

from selenium import webdriver
import datetime
import time
import random

driver = webdriver.PhantomJS('/Users/dannihong/Downloads/phantomjs-2.1.1-macosx/bin/phantomjs')
driver.set_window_size(1280, 2400)

url = 'https://www.bing.com'
driver.get(url)

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.support.expected_conditions as ec

try:
    element = WebDriverWait(driver, 10).until(
        ec.presence_of_element_located
    )








