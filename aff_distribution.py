import sqlite3
import pandas as pd
import datetime
import numpy as np

dbpath = '/Users/Ken/affiliates_data.db'
conn = sqlite3.connect(dbpath)
af_sales = pd.read_sql_query('SELECT Tier1AffiliateID,Commission FROM affiliate_data',conn)
af_date = pd.read_sql_query('SELECT Tier1AffiliateID,Date FROM affiliate_list',conn)
conn.close()


af_sales = pd.pivot_table(af_sales,values='Commission',index='Tier1AffiliateID',aggfunc=np.sum)#アフィリエイターIDごとに報酬の合計を集計
d_today = datetime.date.today()#今日の日付取得
d_today=d_today.strftime('%Y/%m/%d')
d_today = datetime.datetime.strptime(d_today, '%Y/%m/%d')



df = pd.merge(af_date,af_sales,on='Tier1AffiliateID')

df.to_excel('/Users/Ken/Downloads/affiliate_deistribution.xlsx')
date_delta=[]
date_list = af_date['Date'].to_list()
for i in date_list:
    i = datetime.datetime.strptime(i, '%Y/%m/%d')
    delta = d_today-i
    date_delta.append(delta.days)
