from selenium import webdriver
import datetime
import time
  
  
def login():
  # 打开淘宝登录页，并进行扫码登录
    browser.get("https://www.jd.com/")
    time.sleep(3)
    browser.find_element_by_xpath('//*[@id="ttbar-login"]/a[1]').click()
#   if browser.find_element_by_link_text("亲，请登录"):
#     browser.find_element_by_link_text("亲，请登录").click()
    print("请在15秒内完成扫码")
    time.sleep(15)
    browser.get("https://cart.jd.com/cart_index/")
    time.sleep(3)
    
    now = datetime.datetime.now()
    print('login success:', now.strftime('%Y-%m-%d %H:%M:%S'))
  
  
def buy(times, choose):

    while True:
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        # 对比时间，时间到的话就点击结算
        if now > times:
            
            if choose == 1:
                # while True:
                    # try:
                    #     if browser.find_element_by_xpath('//*[@id="cart-body"]/div[1]/div[4]/div[1]/div/input'):
                    #         browser.find_element_by_xpath('//*[@id="cart-body"]/div[1]/div[4]/div[1]/div/input').click()
                    #         break
                    # except:
                    #     print("找不到购买按钮")
                while True:              
                    if browser.find_element_by_xpath('//*[@id="cart-body"]/div[1]/div[5]/div/div[2]/div/div/div/div[2]/div[2]/div/div[1]/a'):
                        browser.find_element_by_xpath('//*[@id="cart-body"]/div[1]/div[5]/div/div[2]/div/div/div/div[2]/div[2]/div/div[1]/a').click()
                        break                           
                                                        #
    browser.get('https://trade.jd.com/shopping/order/getOrderInfo.action')
    if browser.find_element_by_xpath('//*[@id="order-submit"]'):
        browser.find_element_by_xpath('//*[@id="order-submit"]').click()

if __name__ == "__main__":
    times = input("请输入抢购时间，格式如(2018-09-06 11:20:00.000000):")
  # 时间格式："2021-03-31 09:50:00.000000"
    browser = webdriver.Edge()
    browser.maximize_window()
    login()
    choose = int(input("到时间自动勾选购物车请输入“1”，否则输入“2”："))
    buy(times, choose)

    
