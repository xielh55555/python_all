# coding='utf-8'
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

browser=webdriver.Edge()
browser.maximize_window()
browser.get('http://oa.highly.com.cn/login.jsp')

browser.find_element_by_name('j_username').send_keys('xielh')
browser.find_element_by_name('j_password').send_keys('XLh19841022')
browser.find_element_by_name('j_password').send_keys(Keys.ENTER)

el=browser.find_element_by_xpath("//div[@data-portal-id='1680248a43ec802845eb3c443cf84f80']")
browser.execute_script("arguments[0].click();", el)

browser.close()
n=browser.window_handles
browser.switch_to.window(n[0])


# js="document.getElementsByClassName('sub-menu')[3].style.display='block'"
# browser.execute_script(js)

# el=browser.find_element_by_id('link_ORDER_QUERY')
# browser.execute_script("arguments[0].click();",el)
# browser.switch_to_frame('iframe_ORDER_QUERY')

# browser.find_element_by_xpath('//*[@id="query-form"]/div[1]/div[3]/div/div/div/div').click()
# browser.find_element_by_xpath('//*[@id="query-form"]/div[1]/div[3]/div/div/div/div/input').send_keys('湖南省')
# time.sleep(0.3)
# browser.find_element_by_xpath('//*[@id="query-form"]/div[1]/div[3]/div/div/div/div/input').send_keys(Keys.ENTER)

# browser.find_element_by_xpath('//*[@id="query-form"]/div[2]/div[1]/div/div/div/div').click()
# browser.find_element_by_xpath('//*[@id="query-form"]/div[2]/div[1]/div/div/div/div/input').send_keys('LENOVO_消费')
# time.sleep(0.3)
# browser.find_element_by_xpath('//*[@id="query-form"]/div[2]/div[1]/div/div/div/div/input').send_keys(Keys.ENTER)
# time.sleep(0.3)
# browser.find_element_by_xpath('//*[@id="query"]').click()

js="document.getElementsByClassName('sub-menu')[0].style.display='block'"
browser.execute_script(js)
el=browser.find_element_by_id('link_FR_OM_XSFF')
browser.execute_script("arguments[0].click();",el)
browser.switch_to_frame('lcm-frame')
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div[1]/input').clear()

/html/body/div[1]/div[1]/div[2]/div/div[2]/div[1]/input

