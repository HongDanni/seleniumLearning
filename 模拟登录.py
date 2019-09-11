# -*-coding;utf8-*-

from selenium import webdriver
import datetime
import time
import random

driver = webdriver.PhantomJS('/Users/dannihong/Downloads/phantomjs-2.1.1-macosx/bin/phantomjs')
driver.set_window_size(1280, 2400)
def savepic():
    # 存储网页快照图片
    base_dir = '/Users/dannihong/Downloads/seleniumLearning/imgs/'
    filename = '{}{:%Y%m%d%H%M%S}-{:03}.png'.format(base_dir, datetime.datetime.now(), random.randint(1, 999))
    # 触发网页快照行为
    driver.save_screenshot(filename)


url = 'https://www.oschina.net/home/login'
driver.get(url)
savepic()  # 没有输入用户名和密码的网页截图



# 通过id获取两个元素（用户名和密码）
email = driver.find_element_by_id('userMail')
password = driver.find_element_by_id('userPassword')

# 模拟键盘输入数据（输入用户名和密码）
email.send_keys('16675143051')
password.send_keys('niba4699')
savepic()  # 输入用户名和密码的网页截图

# 输入回车（登录）
from selenium.webdriver.common.keys import Keys
password.send_keys(Keys.ENTER)  # 敲入回车键
time.sleep(2)
savepic()  # 登录后的网页截图
print('url after login : {}'.format(driver.current_url))  # 登录成功后的网页




driver.close()









