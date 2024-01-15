# coding: utf-8

import pandas as pd
from datetime import date, datetime, timedelta
from decimal import Decimal, ROUND_HALF_UP
import matplotlib.pyplot as plt

pd.set_option("display.max.columns", 365)
pd.set_option('display.max_rows', 500)

bk = pd.read_csv('/Users/Ken/Documents/Kiryoku/BK.csv', encoding="utf_8_sig", index_col=0)
kx = pd.read_csv('/Users/Ken/Documents/Kiryoku/KX.csv', encoding="utf_8_sig", index_col=0)
pk = pd.read_csv('/Users/Ken/Documents/Kiryoku/PK.csv', encoding="utf_8_sig", index_col=0)
ud = pd.read_csv('/Users/Ken/Documents/Kiryoku/UD.csv', encoding="utf_8_sig", index_col=0)
#bk_click = pd.read_csv('/Users/Ken/Documents/Kiryoku/BK_clicks.csv', encoding="utf_8_sig", index_col=0)
#kx_click = pd.read_csv('/Users/Ken/Documents/Kiryoku/KX_clicks.csv', encoding="utf_8_sig", index_col=0)
#pk_click = pd.read_csv('/Users/Ken/Documents/Kiryoku/PK_clicks.csv', encoding="utf_8_sig", index_col=0)
#ud_click = pd.read_csv('/Users/Ken/Documents/Kiryoku/UD_clicks.csv', encoding="utf_8_sig", index_col=0)

#kiryoku = [bk]#,kx,pk,ud]
#kiryoku_click = [bk_click] #[bk_click, kx_click, pk_click, ud_click]
names = ['BK','KX','PK','UD']
#fromdate = '2020-01-01'
#todate = '2020-01-07'

#for a in kiryoku_click:
#    a['日付'] = pd.to_datetime(a['日付'])


#週ごとに合計値の変化数
def weekly_sum(site):
    site['日付'] = pd.to_datetime(site['日付'])
    #TypeError: Only valid with DatetimeIndex, TimedeltaIndex or PeriodIndex, but got an instance of 'RangeIndex'というエラーが発生
    #インデックスに指定しなければならない
    site.set_index('日付', inplace=True)
    weekly_data = site.resample(rule = 'W').sum()
    #まずは最新週と前週との比較
    #dfの行をSeriesに移す
    #インデックスで最後の行と最後から二番目の行を指定
    latest_week = weekly_data.iloc[-1,:]
    last_week = weekly_data.iloc[-2,:]
    weekly_sales_yen = latest_week-last_week
    weekly_sales_per = latest_week/last_week*100

    print('\n'+'先週からの売上変化額')
    print(weekly_sales_yen)
    print('\n'+'B先週からの売上変化%')
    print(weekly_sales_per)
    print('\n'+'\n')
#週毎の平均値の変化
def weekly_mean(site):
    site['日付'] = pd.to_datetime(site['日付'])
    #TypeError: Only valid with DatetimeIndex, TimedeltaIndex or PeriodIndex, but got an instance of 'RangeIndex'というエラーが発生
    #インデックスに指定しなければならない
    site.set_index('日付', inplace=True)
    weekly_data = site.resample(rule = 'W').mean()
    #まずは最新週と前週との比較
    #dfの行をSeriesに移す
    #インデックスで最後の行と最後から二番目の行を指定
    latest_week = weekly_data.iloc[-1,:]
    last_week = weekly_data.iloc[-2,:]
    weekly_sales_yen = latest_week-last_week
    weekly_sales_per = latest_week/last_week
    #どのくらい変化があったか
    print('\n'+'先週からの平均売上変化額')
    print(weekly_sales_yen)
    print('\n'+'先週からの平均売上変化%')
    print(weekly_sales_per)
    print('\n'+'\n')
def daily_cvr(site,site_click, fromdate, todate):
    site['日付'] = pd.to_datetime(site['日付'])
    df = site[(site['日付'] >= fromdate ) & (site['日付'] <= todate)]
    df = pd.pivot_table(df, index = 'アフィリエイトID', columns='日付', values='報酬', aggfunc='sum')
    print(df.round(0))
    df.to_csv('/Users/Ken/Documents/Kiryoku/data.csv')
def weekly_cvr(site,site_click):
    site['日付'] = pd.to_datetime(site['日付'])
    site.set_index('日付', inplace=True)
    df = site['注文ID'].str.split('_',1,expand = True)
    df.columns = ['注文ID','その他']
    df = df.drop('その他', axis=1)
    df = df.drop_duplicates(subset = '注文ID')
    weekly_data = df.resample(rule = 'W').count()
    #
    site_click['日付'] = pd.to_datetime(site_click['日付'])
    site_click.set_index('日付', inplace=True)
    number_click = site_click.resample(rule = 'W').count()
    number_click = list(number_click['アフィリエイター'])
    weekly_data['クリック数']=number_click
    weekly_data['CVR'] = (weekly_data['注文ID']/weekly_data['クリック数'])*100
    weekly_data['CVR'] = weekly_data['CVR'].map(lambda x: float(Decimal(str(x))
                            .quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)))
    weekly_data.rename({'注文ID':'注文数'}, axis = 1)
    print(weekly_data)

def monthly_cvr(site,site_click):
    site['日付'] = pd.to_datetime(site['日付'])
    site.set_index('日付', inplace=True)
    df = site['注文ID'].str.split('_',1,expand = True)
    df.columns = ['注文ID','その他']
    df = df.drop('その他', axis=1)
    df = df.drop_duplicates(subset = '注文ID')
    weekly_data = df.resample(rule = 'M').count()
    #
    site_click['日付'] = pd.to_datetime(site_click['日付'])
    site_click.set_index('日付', inplace=True)
    number_click = site_click.resample(rule = 'M').count()
    number_click = list(number_click['アフィリエイター'])
    weekly_data['クリック数']=number_click
    weekly_data['CVR'] = (weekly_data['注文ID']/weekly_data['クリック数'])*100
    weekly_data['CVR'] = weekly_data['CVR'].map(lambda x: float(Decimal(str(x))
                            .quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)))
    weekly_data.rename({'注文ID':'注文数'}, axis = 1)
    print(weekly_data)

def unit_sales(site):
    site['日付'] = pd.to_datetime(site['日付'])
    site.set_index('日付', inplace=True)
    weekly_data = site['販売価格'].resample(rule = 'W').sum() / site['販売価格'].resample(rule = 'W').count()
    print(weekly_data)
def item_sales(site):
    site['日付'] = pd.to_datetime(site['日付'])
    site.set_index('日付', inplace=True)
    df = site.query('商品名 == "Vウォッシュ プラス100ml"')
    print(df['販売価格'])
    y = df['販売価格'].resample(rule = 'W').sum()
    y.plot(title='Vウォッシュ プラス100ml')
    plt.show()

bk['日付'] = pd.to_datetime(bk['日付'])
bk.set_index('日付', inplace=True)
bkk = bk[bk(['日付'] >= '2020/03/01')&(['日付'] <= '2021/06/30')]
bkk.to_csv('/Users/Ken/Downloads/bk_Mar_Jun.csv',index_col=0)


#df[df['カラム名']=='抽出条件']

#bk['最初のリファラ'] = bk['最初のリファラ'].str.split('?', expand=True)

#print(bk['最初のリファラ'].str.contains('instagram'))
