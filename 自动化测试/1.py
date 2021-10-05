# coding='utf-8'
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

browser=webdriver.Edge()
browser.get('http://oa.highly.com.cn/login.jsp')
print(browser.title)

browser.find_element_by_name('j_username').send_keys('xielh')
browser.find_element_by_name('j_password').send_keys('XLh19841022')
browser.find_element_by_name('j_password').send_keys(Keys.ENTER)
print(browser.title)
el=browser.find_element_by_xpath("//div[@data-portal-id='1680248a43ec802845eb3c443cf84f80']")
browser.execute_script("arguments[0].click();", el)
print(browser.title)
browser.close()
n=browser.window_handles
browser.switch_to.window(n[0])
print(browser.title)

js="document.getElementsByClassName('sub-menu')[3].style.display='block'"
browser.execute_script(js)
# el = WebDriverWait(browser, 10).until(
#         EC.presence_of_element_located((By.XPATH, "//*[@id='page-sidebar-menu']/li[4]"))
#     )
# /*[@id='page-sidebar-menu']/li[4]/ul
# el=browser.find_element_by_xpath("//*[@id='page-sidebar-menu']/li[4]")
# browser.execute_script('arguments[0].click();',el)
el=browser.find_element_by_id('link_ORDER_QUERY')
browser.execute_script("arguments[0].click();",el)
browser.switch_to_frame('iframe_ORDER_QUERY')
name=browser.find_elements_by_tag_name('tr')
nlist=[]
for tr in name:
    tdlist=tr.find_elements_by_tag_name('td')
    if len(tdlist)>0:
        tdlist=tr.find_elements_by_tag_name('td')
        for nn in tdlist:
            nnx=nn.text
            nlist.append(nnx)
        print(nlist)
        nlist=[]
for tr in name:
    tdlist=tr.find_elements_by_tag_name('th')
    if len(tdlist)>0:
        tdlist=tr.find_elements_by_tag_name('th')
        for nn in tdlist:
            nnx=nn.text
            nlist.append(nnx)
        print(nlist)
        nlist=[]
# x=yy.get()
# browser.find_element_by_id('ecsOrderCode').send_keys('wq vb  f djksadf ')
browser.find_element_by_xpath('//*[@id="query-form"]/div[1]/div[3]/div/div/div/div').click()
browser.find_element_by_xpath('//*[@id="marketProvinceId"]/option[1]').click()
# browser.find_element_by_css_selector('#marketProvinceId > option:nth-child(1)').click()
# browser.find_element_by_xpath('//*[@id="marketProvinceId"]/option[1]').click()

# Select(browser.find_element_by_xpath('//*[@id="marketProvinceId"]')).select_by_value('10061')
# loc = (By.XPATH, '//a[text()="湖南省"]')
# WebDriverWait(browser, 10).until(EC.visibility_of_element_located(loc))
# browser.find_element_by_xpath('//a[text()="湖南省"]').click()

# Select(browser.find_element_by_xpath('//*[@id="query-form"]/div[2]/div[3]/div/div/span/select')).select_by_value('N')
# browser.find_element_by_xpath("//*[@id='query-form']/div[1]/div[3]/div/div/div/div/input").send_keys('湖南省')
# browser.find_element_by_id('marketProvinceId').select
print('结束了。。。？')

# browser.find_element_by_xpath()
# browser.quit()
# /html/body/div[5]/div[2]/div/div[2]/div[2]/div/div[2]/iframe
# /html/body/div[1]/div[1]/form/div[1]/div[1]/div[3]/div