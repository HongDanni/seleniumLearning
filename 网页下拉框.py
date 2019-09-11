# coding: utf8
from selenium import webdriver
import datetime
import time
import random

# 创建核心对象
driver = webdriver.PhantomJS('/Users/dannihong/Downloads/phantomjs-2.1.1-macosx/bin/phantomjs')
# 设置分辨率
driver.set_window_size(1028, 2400)

# 截图
def savepic():
    # 存储网页快照图片
    base_dir = '/Users/dannihong/Documents/myproject/seleniumTest/imgs/'
    filename = '{}{:%Y%m%d%H%M%S}.png'.format(base_dir, datetime.datetime.now())
    # 触发网页快照行为
    # filename = '1.jpg'
    driver.save_screenshot(filename)

# 网址
url = 'https://www.oschina.net/search?q=python&scope=project'
# 访问网址
driver.get(url)
# 截图
savepic()
time.sleep(3)
savepic()

driver.close()  # driver要关闭










