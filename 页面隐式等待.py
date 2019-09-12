# -*-coding:utf8-*-

from selenium import webdriver
import datetime

driver = webdriver.PhantomJS('/Users/dannihong/Downloads/phantomjs-2.1.1-macosx/bin/phantomjs')
driver.set_window_size(1280, 2400)
driver.implicitly_wait(10)  # 全局设置，会导致下面找元素等待10秒；即driver遇到No Such Element 都会停下来等10秒

url = 'https://movie.douban.com/'
driver.get(url)


try:
    print('start_time: {}'.format(datetime.datetime.now()))
    waite_element = driver.find_element_by_id('124')
    print('element: {}'.format(waite_element))
    print('get_element_time: {}'.format(datetime.datetime.now()))

except Exception as e:
    # 等待10秒后，仍然没找到该元素，抛出异常
    print('throw_error_time: {}'.format(datetime.datetime.now()))
    print('error message: {}; error type: {}'.format(e, type(e)))
finally:
    driver.quit()



