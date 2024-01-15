import requests
from bs4 import BeautifulSoup
import time
import urllib
import pandas as pd
from requests_html import HTML, HTMLSession
import sqlite3
import time
import random
# Webページを取得して解析する

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
}
"""
#Fetch multiple site
sites = []
dbpath = '/Users/Ken/affiliates_data.db'
conn = sqlite3.connect(dbpath)
df=pd.read_sql_query('SELECT * FROM affiliate_list',conn)
conn.close()

df = df[~df['Website1'].str.contains('twitter',na=False)]
df = df[~df['Website1'].str.contains('instagram',na=False)]
df = df[~df['Website1'].str.contains('tiktok',na=False)]
df = df[~df['Website1'].str.contains('lemon8',na=False)]
df = df[~df['Website1'].str.contains('youtube',na=False)]
df = df[~df['Website1'].str.contains('facebook',na=False)]
df = df[~df['Website1'].str.contains('google',na=False)]
df = df[~df['Website1'].str.contains('monetrack',na=False)]
#df.to_excel('/Users/Ken/Downloads/page_count_list.xlsx')
"""
df = pd.read_excel('/Users/Ken/Downloads/page_count_list.xlsx', engine='openpyxl')
df = df[df['Page_count'].isnull()]


def parse_html(url):
    load_url = ("https://www.google.com/search?q=site%3A" + url)
    html = requests.get(load_url,headers=headers)
    sec = random.uniform(5,15)
    time.sleep(sec)
    soup = BeautifulSoup(html.content, "html.parser")
    count = soup.find(id='result-stats').text
    count = int(count.split(' ')[1].replace(',',''))
    return count

a = 1
for i in range(1,len(df)):#177
    try:
        page_count = parse_html(df.iloc[i,3])
        print(df.iloc[i,3],page_count)
        sec = random.uniform(10,60)
        time.sleep(sec)
        a += 1
        if a % 40 == 0:
            time.sleep(120)
        elif a == 70 or a == 120:
            time.sleep(70)
    except IndexError:
        print(df.iloc[i,3],'Pass')
    except ValueError:
        print(df.iloc[i,3],'Pass')
    except TypeError:
        print(df.iloc[i,3],'Pass')
