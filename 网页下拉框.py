# coding:utf8
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
    base_dir = '/Users/dannihong/Downloads/seleniumLearning/imgs/'
    filename = '{}{:%Y%m%d%H%M%S}.png'.format(base_dir, datetime.datetime.now())
    # 触发网页快照行为
    # filename = '1.jpg'
    driver.save_screenshot(filename)

url = 'https://www.oschina.net/search?q=python&scope=project'
driver.get(url)  # 访问网址
print(driver.current_url)
# savepic()


ele = driver.find_element_by_name('tag1')
print(ele)
print(type(ele))

driver.close()  # driver要关闭










