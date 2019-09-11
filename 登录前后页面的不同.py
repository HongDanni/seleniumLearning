# -*-coding;utf8-*-

from selenium import webdriver
import datetime
import time
import random

driver = webdriver.PhantomJS('/Users/dannihong/Downloads/phantomjs-2.1.1-macosx/bin/phantomjs')
driver.set_window_size(1280, 2400)

# 登录之前，页面右上角的显示mobileUserSidebar
url = 'https://www.oschina.net'
driver.get(url)
useinfo = driver.find_element_by_id('mobileUserSidebar')
print(useinfo)
print(useinfo.text)


driver.close()


