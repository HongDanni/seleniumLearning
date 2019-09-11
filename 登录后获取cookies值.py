# -*-coding;utf8-*-

from selenium import webdriver
import datetime
import time
import random

driver = webdriver.PhantomJS('/Users/dannihong/Downloads/phantomjs-2.1.1-macosx/bin/phantomjs')
driver.set_window_size(1280, 2400)

url = 'https://www.oschina.net/home/login'
driver.get(url)

email = driver.find_element_by_id('userMail')
password = driver.find_element_by_id('userPassword')

email.send_keys('16675143051')
password.send_keys('niba4699')

from selenium.webdriver.common.keys import Keys
password.send_keys(Keys.ENTER)

cookies = driver.get_cookies()
print('cookies: {}'.format(cookies))




