from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains as chains
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from bs4 import BeautifulSoup
import time
import datetime
from urllib import request
import pandas as pd


merchants_name = []
merchants_name2 = []
merchants_sales = []

#Open browser
options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome(executable_path='/Users/Ken/Downloads/chromedriver', options = options) #, options = options
#Open Monetrack login
driver.get("https://app.monetrack.com/ja")
#maximize window
driver.maximize_window()

#Wait for 3 sec
time.sleep(3)
#Login
login_id = driver.find_element_by_xpath("//input[@id='user_email']")
login_id.send_keys("admin@monetrack.com")

#Wait for 3 sec
time.sleep(1)

password = driver.find_element_by_xpath("//input[@id='user_password']")
password.send_keys("Saba2021")

#Wait for 1 sec
driver.implicitly_wait(1)

#specify with class
btn = driver.find_element_by_class_name("mb-0")
btn.click()

time.sleep(2)

#承認へ
drop_down_xpath = '//a[@class="waves-effect"]'
option_xpath = '//span[text()="承認"]'
chain = chains(driver)
chain.move_to_element(driver.find_element_by_xpath(drop_down_xpath)).move_to_element(driver.find_element_by_xpath(option_xpath)).click().perform()
time.sleep(1)


while True:
    try:
        #テーブルにアクセス
        table = driver.find_element_by_xpath('//*[@id="page-wrapper"]/div[2]/div/div/div')
        #テーブル業取得
        tablerow = table.find_element_by_xpath('//*[@id="merchants-table"]/tbody/tr[1]')
        nums = range(1, 26)
        for num in nums:
            get_merchants_name = tablerow.find_element_by_xpath('//*[@id="merchants-table"]/tbody/tr['+str(num)+']/td[2]')
            #リストにMerchant名追加
            merchants_name.append(get_merchants_name.text)
        #Move on to next page
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(0.5)
        next_page = driver.find_element_by_xpath('//*[@id="merchants-table_paginate"]/ul/li[8]/a')
        next_page.click()
        time.sleep(3)
    except NoSuchElementException:
        break

for item in merchants_name:
    item_mod = item.replace("SIX-CHANGE", "six change")
    merchants_name2.append(item_mod)

#Scroll Up
driver.execute_script("window.scrollTo(1000, 0)")
time.sleep(1)

try:
    for i in merchants_name2:
        #Search bestkenko
        search = driver.find_element_by_xpath('//*[@id="merchants-table_filter"]/label/input')
        search.send_keys(i)
        time.sleep(1)
        #Press Return key
        search.send_keys(Keys.RETURN)
        time.sleep(5)
        #テーブルにアクセス
        table = driver.find_element_by_xpath('//*[@id="page-wrapper"]/div[2]/div/div/div')
        #テーブル業取得
        tablerow = table.find_element_by_xpath('//*[@id="merchants-table"]')
        #Loginして売上Get
        merchant_login = driver.find_element_by_xpath('//*[@id="merchants-table"]/tbody/tr/td[8]/div/a[3]')
        merchant_login.click()
        time.sleep(1)
        merchant_login2_bk = driver.find_element_by_xpath('/html/body/div[6]/div/div/div[2]/button[2]')
        merchant_login2_bk.click()
        #wait for 2 secs
        time.sleep(4)
        #Scroll down
        driver.execute_script("window.scrollTo(0, 1000)")
        weeklysales = driver.find_element_by_xpath('//*[@id="page-wrapper"]/div[2]/div/div[4]/div[2]/div/div[1]/h1')
        merchants_sales.append(weeklysales.text)
        #Scroll Up
        driver.execute_script("window.scrollTo(1000, 0)")
        time.sleep(1)
        #Go back to admin
        back_to_admin = driver.find_element_by_class_name("back-to-admin")
        back_to_admin.click()
        time.sleep(3)
        #承認へ
        drop_down_xpath = '//a[@class="waves-effect"]'
        option_xpath = '//span[text()="承認"]'
        chain = chains(driver)
        chain.move_to_element(driver.find_element_by_xpath(drop_down_xpath)).move_to_element(driver.find_element_by_xpath(option_xpath)).click().perform()
        time.sleep(3)
except TimeoutException:
    pass
except NoSuchElementException:
    pass

df = pd.DataFrame(merchants_name2, columns=['Merchants'])
df2 = pd.DataFrame(merchants_sales, columns=['Weekly Sales'])

df[1]=df2

df.to_csv('/Users/Ken/Downloads/UD.csv', mode='a', header=False)

"""
リスト内容その書き換え
https://www.sejuku.net/blog/66949
"""
