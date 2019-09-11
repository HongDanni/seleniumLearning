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
url = 'https://cn.bing.com/search?q=hello'
# 访问网址
driver.get(url)
# 截图
def savepic():
    # 存储网页快照图片
    base_dir = '/Users/dannihong/Documents/myproject/seleniumTest/imgs/'
    filename = '{}{:%Y%m%d%H%M%S}{:02}.png'.format(base_dir, datetime.datetime.now(), random.randint(10, 99))
    # 触发网页快照行为
    # filename = '1.jpg'
    driver.save_screenshot(filename)


# savepic()

# 方案1
# 等页面加载出来后，再进行截图
# time.sleep(5)
# savepic()

# 设置尝试的次数
# 查找DOM树里的元素意味着通过ajax返回的需要的内容加载了出来
MAXRETRIES = 5
while MAXRETRIES:
    try:
        ele = driver.find_element_by_id('b_results')
        print('******')
        print('element: {}, maxretries: {}'.format(ele, MAXRETRIES))
        savepic()  # 如果页面完全加载出来，截图快照
        break
    except Exception as e:
        print('^^^^^^')
        print('error message: {}, error type: {}'.format(e, type(e)))
        time.sleep(1)  #暂停1秒
    MAXRETRIES -= 1


driver.close()  # driver要关闭 










