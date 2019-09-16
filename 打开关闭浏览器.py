# -*- coding:utf8 -*-

from selenium import webdriver
import datetime
import time
import random

def savepic():
    # 存储网页快照图片
    base_dir = '/Users/dannihong/Downloads/seleniumLearning/imgs/'
    filename = '{}{:%Y%m%d%H%M%S}-{:03}.png'.format(base_dir, datetime.datetime.now(), random.randint(1, 999))
    # 触发网页快照行为
    driver.save_screenshot(filename)


driver = webdriver.PhantomJS('../phantomjs-2.1.1-macosx/bin/phantomjs')
# driver.set_window_size(1280, 2400)  # 设置窗口的大小
driver.maximize_window()  # 最大化窗口

url = 'https://www.oschina.net/home/login'
# driver.get(url)  # 打开url：等待page load完成；无法进行前进后退操作
# print('current url: {}; title: {}; name: {}; mobile: {}'.format(driver.current_url, driver.title, driver.name, driver.mobile))
# savepic()
# driver.close()  # 关闭当前的浏览器窗口
# driver.quit()  # 不仅关闭窗口，还会彻底的退出webdriver，释放与driver server之间的连接


driver.g






