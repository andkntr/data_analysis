from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains as chains
import time
from datetime import datetime, date, timedelta
from selenium.webdriver.chrome.options import Options


#Last Monday
fd = date.today() - timedelta(days=7)
td = fd + timedelta(days = 6)

#Change to string
from_date = datetime.strftime(fd, '%Y-%m-%d')
to_date = datetime.strftime(td, '%Y-%m-%d')

options = Options()
options.add_argument('--headless')

#Open browser
driver = webdriver.Chrome(executable_path='/Users/Ken/Downloads/chromedriver 3')#, options = options
#Open Monetrack login
driver.get("https://app.monetrack.com/ja")

#Wait for 3 sec
time.sleep(3)
#Login
login_id = driver.find_element_by_xpath("//input[@id='user_email']")
login_id.send_keys("admin@monetrack.com")

#Wait for 3 sec
time.sleep(3)

password = driver.find_element_by_xpath("//input[@id='user_password']")
password.send_keys("")

#Wait for 3 sec
driver.implicitly_wait(3)

#specify with class
btn = driver.find_element_by_class_name("mb-0")
btn.click()

#wait for 5sec
time.sleep(5)

#Hover to Approved
drop_down_xpath = '//a[@class="waves-effect"]'
option_xpath = '//span[text()="承認"]'
chain = chains(driver)
chain.move_to_element(driver.find_element_by_xpath(drop_down_xpath)).move_to_element(driver.find_element_by_xpath(option_xpath)).click().perform()

#wait for 3sec
time.sleep(3)

#Search bestkenko
merchant_bk = driver.find_element_by_xpath('//*[@id="merchants-table_filter"]/label/input')
merchant_bk.send_keys("bestkenko")
#Press Return key
merchant_bk.send_keys(Keys.RETURN)

#wait for 5 sec
time.sleep(5)

#Login to BK
login_bk = driver.find_element_by_xpath('//*[@id="merchants-table"]/tbody/tr/td[8]/div/a[3]')
login_bk.click()

#wait for 3 secs
time.sleep(3)

#Click to Login to BK Dashboard
login2_bk = driver.find_element_by_xpath('/html/body/div[6]/div/div/div[2]/button[2]')
login2_bk.click()

#wait for 3 sec
time.sleep(3)

#Move to transaction
transaction_bk = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div/ul/li[4]/a")
transaction_bk.click()

#wait for 5 sec
time.sleep(5)

#Open 検索詳細
detail_bk = driver.find_element_by_class_name('advance-search-trigger') #btn btn-success transaction-advance-search-btn
detail_bk.click()

#Scroll down
driver.execute_script("window.scrollTo(0, 500)")

time.sleep(3)

#JavaScriptを使ってBootstrap-datepickerの日付選択 (changeDateがうまく行かない)
#driver.execute_script("document.getElementById('fromdate').value = '11/16/2020'")
#time.sleep(1)
#driver.execute_script("$('#fromdate').datepicker().trigger('changeDate');")
#time.sleep(1)
#driver.execute_script("document.getElementById('todate').value = '11/22/2020'")
#time.sleep(1)
#driver.execute_script("$('#todate').datepicker().trigger('changeDate');")
#time.sleep(4)

#マニュアルで日付選択
#https://python5.com/q/qnybcmep
open_calendar1 = driver.find_element_by_xpath('//*[@id="fromdate"]')
open_calendar1.click()
time.sleep(3)
from_date_cal = driver.find_element_by_xpath("/html/body/div[6]/div[1]/table/tbody/tr/td[text()='5']")
from_date_cal.click()
time.sleep(3)
open_calendar2 = driver.find_element_by_xpath('//*[@id="todate"]')
open_calendar2.click()
to_date_cal = driver.find_element_by_xpath("/html/body/div[6]/div[1]/table/tbody/tr/td[text()='11']")
to_date_cal.click()
time.sleep(3)

#検索実行
search_date = driver.find_element_by_xpath("/html/body/div[3]/div[3]/div[2]/div/div/div/div[2]/div/form/a[2]")
search_date.click()

time.sleep(10)

#Scroll Up
driver.execute_script("window.scrollTo(500, 10)")

time.sleep(2)
#Download excel
dl_exl_bk = driver.find_element_by_xpath("/html/body/div[3]/div[3]/div[2]/div/div/div/div[1]/div/div[2]/div[2]/a[2]")
dl_exl_bk.click()
time.sleep(2)
dl_exl_bk2 = driver.find_element_by_xpath("/html/body/div[6]/div/div/div[2]/button[2]")
dl_exl_bk2.click()

#Back to admin
time.sleep(60)

back_to_admin = driver.find_element_by_class_name("back-to-admin")
back_to_admin.click()

time.sleep(5)

#KX from here

#Hover to Approved
drop_down_xpath = '//a[@class="waves-effect"]'
option_xpath = '//span[text()="承認"]'
chain = chains(driver)
chain.move_to_element(driver.find_element_by_xpath(drop_down_xpath)).move_to_element(driver.find_element_by_xpath(option_xpath)).click().perform()

#wait for 3sec
time.sleep(3)

#Search bestkenko
merchant_kx = driver.find_element_by_xpath('//*[@id="merchants-table_filter"]/label/input')
merchant_kx.send_keys("kusuriexpress")
#Press Return key
merchant_kx.send_keys(Keys.RETURN)

#wait for 5 sec
time.sleep(5)

#Login to BK
login_kx = driver.find_element_by_xpath('//*[@id="merchants-table"]/tbody/tr/td[8]/div/a[3]')
login_kx.click()

#wait for 3 secs
time.sleep(3)

#Click to Login to BK Dashboard
login2_kx = driver.find_element_by_xpath('/html/body/div[6]/div/div/div[2]/button[2]')
login2_kx.click()

#wait for 3 sec
time.sleep(3)

#Move to transaction
transaction_kx = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div/ul/li[4]/a")
transaction_kx.click()

#wait for 5 sec
time.sleep(5)

#Open 検索詳細
detail_kx = driver.find_element_by_class_name('advance-search-trigger') #btn btn-success transaction-advance-search-btn
detail_kx.click()

#Scroll down
driver.execute_script("window.scrollTo(0, 500)")

time.sleep(3)

#マニュアルで日付選択
#https://python5.com/q/qnybcmep
open_calendar1 = driver.find_element_by_xpath('//*[@id="fromdate"]')
open_calendar1.click()
time.sleep(3)
from_date_cal = driver.find_element_by_xpath("/html/body/div[6]/div[1]/table/tbody/tr/td[text()='5']")
from_date_cal.click()
time.sleep(3)
open_calendar2 = driver.find_element_by_xpath('//*[@id="todate"]')
open_calendar2.click()
to_date_cal = driver.find_element_by_xpath("/html/body/div[6]/div[1]/table/tbody/tr/td[text()='11']")
to_date_cal.click()
time.sleep(3)

#検索実行
search_date = driver.find_element_by_xpath("/html/body/div[3]/div[3]/div[2]/div/div/div/div[2]/div/form/a[2]")
search_date.click()

time.sleep(10)

#Scroll Up
driver.execute_script("window.scrollTo(500, 10)")

time.sleep(2)
#Download excel
dl_exl_kx = driver.find_element_by_xpath("/html/body/div[3]/div[3]/div[2]/div/div/div/div[1]/div/div[2]/div[2]/a[2]")
dl_exl_kx.click()
time.sleep(2)
dl_exl_kx2 = driver.find_element_by_xpath("/html/body/div[6]/div/div/div[2]/button[2]")
dl_exl_kx2.click()

#Back to admin
time.sleep(60)

back_to_admin = driver.find_element_by_class_name("back-to-admin")
back_to_admin.click()

time.sleep(5)

#PK from here

#Hover to Approved
drop_down_xpath = '//a[@class="waves-effect"]'
option_xpath = '//span[text()="承認"]'
chain = chains(driver)
chain.move_to_element(driver.find_element_by_xpath(drop_down_xpath)).move_to_element(driver.find_element_by_xpath(option_xpath)).click().perform()

#wait for 3sec
time.sleep(3)

#Search bestkenko
merchant_pk = driver.find_element_by_xpath('//*[@id="merchants-table_filter"]/label/input')
merchant_pk.send_keys("petkusuri")
#Press Return key
merchant_pk.send_keys(Keys.RETURN)

#wait for 5 sec
time.sleep(5)

#Login to BK
login_pk = driver.find_element_by_xpath('//*[@id="merchants-table"]/tbody/tr/td[8]/div/a[3]')
login_pk.click()

#wait for 3 secs
time.sleep(3)

#Click to Login to BK Dashboard
login2_pk = driver.find_element_by_xpath('/html/body/div[6]/div/div/div[2]/button[2]')
login2_pk.click()

#wait for 3 sec
time.sleep(3)

#Move to transaction
transaction_pk = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div/ul/li[4]/a")
transaction_pk.click()

#wait for 5 sec
time.sleep(5)

#Open 検索詳細
detail_pk = driver.find_element_by_class_name('advance-search-trigger') #btn btn-success transaction-advance-search-btn
detail_pk.click()

#Scroll down
driver.execute_script("window.scrollTo(0, 500)")

time.sleep(3)

#マニュアルで日付選択
#https://python5.com/q/qnybcmep
open_calendar1 = driver.find_element_by_xpath('//*[@id="fromdate"]')
open_calendar1.click()
time.sleep(3)
from_date_cal = driver.find_element_by_xpath("/html/body/div[6]/div[1]/table/tbody/tr/td[text()='5']")
from_date_cal.click()
time.sleep(3)
open_calendar2 = driver.find_element_by_xpath('//*[@id="todate"]')
open_calendar2.click()
to_date_cal = driver.find_element_by_xpath("/html/body/div[6]/div[1]/table/tbody/tr/td[text()='11']")
to_date_cal.click()
time.sleep(3)

#検索実行
search_date = driver.find_element_by_xpath("/html/body/div[3]/div[3]/div[2]/div/div/div/div[2]/div/form/a[2]")
search_date.click()

time.sleep(10)

#Scroll Up
driver.execute_script("window.scrollTo(500, 10)")

time.sleep(2)
#Download excel
dl_exl_pk = driver.find_element_by_xpath("/html/body/div[3]/div[3]/div[2]/div/div/div/div[1]/div/div[2]/div[2]/a[2]")
dl_exl_pk.click()
time.sleep(2)
dl_exl_pk2 = driver.find_element_by_xpath("/html/body/div[6]/div/div/div[2]/button[2]")
dl_exl_pk2.click()

#Back to admin
time.sleep(60)

back_to_admin = driver.find_element_by_class_name("back-to-admin")
back_to_admin.click()

time.sleep(5)

#UD from here

#Hover to Approved
drop_down_xpath = '//a[@class="waves-effect"]'
option_xpath = '//span[text()="承認"]'
chain = chains(driver)
chain.move_to_element(driver.find_element_by_xpath(drop_down_xpath)).move_to_element(driver.find_element_by_xpath(option_xpath)).click().perform()

#wait for 3sec
time.sleep(3)

#Search bestkenko
merchant_ud = driver.find_element_by_xpath('//*[@id="merchants-table_filter"]/label/input')
merchant_ud.send_keys("unidru")
#Press Return key
merchant_ud.send_keys(Keys.RETURN)

#wait for 5 sec
time.sleep(5)

#Login to BK
login_ud = driver.find_element_by_xpath('//*[@id="merchants-table"]/tbody/tr/td[8]/div/a[3]')
login_ud.click()

#wait for 3 secs
time.sleep(3)

#Click to Login to BK Dashboard
login2_ud = driver.find_element_by_xpath('/html/body/div[6]/div/div/div[2]/button[2]')
login2_ud.click()

#wait for 3 sec
time.sleep(3)

#Move to transaction
transaction_ud = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div/ul/li[4]/a")
transaction_ud.click()

#wait for 5 sec
time.sleep(5)

#Open 検索詳細
detail_ud = driver.find_element_by_class_name('advance-search-trigger') #btn btn-success transaction-advance-search-btn
detail_ud.click()

#Scroll down
driver.execute_script("window.scrollTo(0, 500)")

time.sleep(3)

#マニュアルで日付選択
#https://python5.com/q/qnybcmep
open_calendar1 = driver.find_element_by_xpath('//*[@id="fromdate"]')
open_calendar1.click()
time.sleep(3)
from_date_cal = driver.find_element_by_xpath("/html/body/div[6]/div[1]/table/tbody/tr/td[text()='5']")
from_date_cal.click()
time.sleep(3)
open_calendar2 = driver.find_element_by_xpath('//*[@id="todate"]')
open_calendar2.click()
to_date_cal = driver.find_element_by_xpath("/html/body/div[6]/div[1]/table/tbody/tr/td[text()='11']")
to_date_cal.click()
time.sleep(3)

#検索実行
search_date = driver.find_element_by_xpath("/html/body/div[3]/div[3]/div[2]/div/div/div/div[2]/div/form/a[2]")
search_date.click()

time.sleep(10)

#Scroll Up
driver.execute_script("window.scrollTo(500, 10)")

time.sleep(2)
#Download excel
dl_exl_ud = driver.find_element_by_xpath("/html/body/div[3]/div[3]/div[2]/div/div/div/div[1]/div/div[2]/div[2]/a[2]")
dl_exl_ud.click()
time.sleep(2)
dl_exl_ud2 = driver.find_element_by_xpath("/html/body/div[6]/div/div/div[2]/button[2]")
dl_exl_ud2.click()

#Back to admin
time.sleep(60)

back_to_admin = driver.find_element_by_class_name("back-to-admin")
back_to_admin.click()

time.sleep(5)


#FM from here

#Hover to Approved
drop_down_xpath = '//a[@class="waves-effect"]'
option_xpath = '//span[text()="承認"]'
chain = chains(driver)
chain.move_to_element(driver.find_element_by_xpath(drop_down_xpath)).move_to_element(driver.find_element_by_xpath(option_xpath)).click().perform()

#wait for 3sec
time.sleep(3)

#Search bestkenko
merchant_fm = driver.find_element_by_xpath('//*[@id="merchants-table_filter"]/label/input')
merchant_fm.send_keys("femito")
#Press Return key
merchant_fm.send_keys(Keys.RETURN)

#wait for 5 sec
time.sleep(5)

#Login to BK
login_fm = driver.find_element_by_xpath('//*[@id="merchants-table"]/tbody/tr/td[8]/div/a[3]')
login_fm.click()

#wait for 3 secs
time.sleep(3)

#Click to Login to BK Dashboard
login2_fm = driver.find_element_by_xpath('/html/body/div[6]/div/div/div[2]/button[2]')
login2_fm.click()

#wait for 3 sec
time.sleep(3)

#Move to transaction
transaction_fm = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div/ul/li[4]/a")
transaction_fm.click()

#wait for 5 sec
time.sleep(5)

#Open 検索詳細
detail_fm = driver.find_element_by_class_name('advance-search-trigger') #btn btn-success transaction-advance-search-btn
detail_fm.click()

#Scroll down
driver.execute_script("window.scrollTo(0, 500)")

time.sleep(3)

#マニュアルで日付選択
#https://python5.com/q/qnybcmep
open_calendar1 = driver.find_element_by_xpath('//*[@id="fromdate"]')
open_calendar1.click()
time.sleep(3)
from_date_cal = driver.find_element_by_xpath("/html/body/div[6]/div[1]/table/tbody/tr/td[text()='5']")
from_date_cal.click()
time.sleep(3)
open_calendar2 = driver.find_element_by_xpath('//*[@id="todate"]')
open_calendar2.click()
to_date_cal = driver.find_element_by_xpath("/html/body/div[6]/div[1]/table/tbody/tr/td[text()='11']")
to_date_cal.click()
time.sleep(3)

#検索実行
search_date = driver.find_element_by_xpath("/html/body/div[3]/div[3]/div[2]/div/div/div/div[2]/div/form/a[2]")
search_date.click()

time.sleep(10)

#Scroll Up
driver.execute_script("window.scrollTo(500, 10)")

time.sleep(2)
#Download excel
dl_exl_fm = driver.find_element_by_xpath("/html/body/div[3]/div[3]/div[2]/div/div/div/div[1]/div/div[2]/div[2]/a[2]")
dl_exl_fm.click()
time.sleep(2)
dl_exl_fm2 = driver.find_element_by_xpath("/html/body/div[6]/div/div/div[2]/button[2]")
dl_exl_fm2.click()

#Back to admin
time.sleep(60)

back_to_admin = driver.find_element_by_class_name("back-to-admin")
back_to_admin.click()

time.sleep(5)


#Referance
#https://techacademy.jp/magazine/28392
#https://techacademy.jp/magazine/21129
#https://kurozumi.github.io/selenium-python/locating-elements.html
#https://sibahublog.com/how-to-handle-when-an-error-occurs-if-there-is-no-element-even-though-the-way-of-writing-pythonxpath-is-specified
#https://www.seleniumqref.com/api/python/element_set/Python_special_send_keys.html
#For drop-down click
#https://stackoverrun.com/ja/q/11160246

#Calendat datepicker
#https://qiita.com/dkugi/items/8c32cc481b365c277ec2
#datepickerの日付入力後のイベント発生
#https://qiita.com/Nod_Y/items/8a47bec834479cd2d010
