# -*-coding;utf8-*-

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

driver = webdriver.PhantomJS('/Users/dannihong/Downloads/phantomjs-2.1.1-macosx/bin/phantomjs')
driver.set_window_size(1280, 2400)

url = 'https://movie.douban.com/'
driver.get(url)

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# 使用WebDriver指定：用哪个driver，等待多久时长；使用EC指定：等到什么样的EC条件；使用By指定：查找网页元素的方法
try:
    element = WebDriverWait(driver, 10).until(  # 10秒为超时时长，超时抛异常，超时时长内在try里默认0.5秒循环执行
        # 方式1：By.ID（通过id查找输入框元素）
        EC.presence_of_element_located((By.ID, "inp-query"))  # 这里要传入的是元组
        # 方式2：By.XPATH
        # EC.presence_of_element_located((By.XPATH, "//input[@id='inp-query']"))
    )  # 默认0.5秒循环一次，查看条件是否达到

    # 模拟在输入框输入'我和我的祖国'，然后回车键开始搜索
    element.send_keys('我和我的祖国')
    element.send_keys(Keys.ENTER)
    print(driver.current_url)  # 跳转到搜索后的url
    savepic()  # 截图查看
except Exception as e:
    print(e)
finally:
    driver.quit()









