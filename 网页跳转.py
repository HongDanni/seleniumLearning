# coding: utf8
from selenium import webdriver
import datetime
import time
import random

# 创建核心对象
driver = webdriver.PhantomJS('/Users/dannihong/Downloads/phantomjs-2.1.1-macosx/bin/phantomjs')
# 设置分辨率
driver.set_window_size(1028, 2400)


# 网址
url = 'http://www.bing.com'
# 访问网址
driver.get(url)
# 实际上跳转的网页
print('refer url: {}'.format(driver.current_url))


driver.close()  # driver要关闭










