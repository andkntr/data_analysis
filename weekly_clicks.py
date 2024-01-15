import pandas as pd
import openpyxl
import datetime
import matplotlib.pyplot as plt

pd.set_option("display.max.columns", 14)

def add_clicks(file, site):
    #週データ読み込み
    df = pd.read_excel(file, engine='openpyxl')


    #日付を分割してデータフレームにする（https://note.nkmk.me/python-pandas-split-extract/
    trans_datetime = df['日付'].str.split(' ', expand=True)
    #インデックスを指定
    trans_datetime.columns = ['日付','時間']
    #時間の列を削除
    trans_date = trans_datetime.drop('時間', axis=1)
    #日付の置き換え
    df['日付'] = trans_date
    df = df.drop('OS', axis=1)
    #既存CSVファイルに追記 https://note.nkmk.me/python-pandas-to-csv/
    df.to_csv('/Users/Ken/Documents/Kiryoku/'+site+'_clicks.csv', mode='a', header=False) #, mode='a', header=False

add_clicks(file='/Users/Ken/Downloads/1617258906_すべてのクリック.xlsx', site = 'KX')


bk_click = pd.read_csv('/Users/Ken/Documents/Kiryoku/BK_clicks.csv', encoding="utf_8_sig", index_col=0)
kx_click = pd.read_csv('/Users/Ken/Documents/Kiryoku/KX_clicks.csv', encoding="utf_8_sig", index_col=0)
#pk_click = pd.read_csv('/Users/Ken/Documents/Kiryoku/PK_clicks.csv', encoding="utf_8_sig", index_col=0)
#ud_click = pd.read_csv('/Users/Ken/Documents/Kiryoku/UD_clicks.csv', encoding="utf_8_sig", index_col=0)

def monthly_clicks(site_click):#, fromdate, todate
    site_click['日付'] = pd.to_datetime(site_click['日付'])
    #TypeError: Only valid with DatetimeIndex, TimedeltaIndex or PeriodIndex, but got an instance of 'RangeIndex'というエラーが発生
    #インデックスに指定しなければならない
    site_click.set_index('日付', inplace=True)
    #weekly_data = site_click[(site_click['日付'] >= fromdate ) & (site_click['日付'] <= todate)]
    number_click = site_click.resample(rule = 'M').count()
    #weekly_data.columns = ['クリック数']
    print(number_click)
    #number_click.plot(title='Weekly Clicks')
    #plt.show()

def weekly_clicks(site_click):#, fromdate, todate
    site_click['日付'] = pd.to_datetime(site_click['日付'])
    #TypeError: Only valid with DatetimeIndex, TimedeltaIndex or PeriodIndex, but got an instance of 'RangeIndex'というエラーが発生
    #インデックスに指定しなければならない
    site_click.set_index('日付', inplace=True)
    #weekly_data = site_click[(site_click['日付'] >= fromdate ) & (site_click['日付'] <= todate)]
    number_click = site_click.resample(rule = 'W').count()
    #weekly_data.columns = ['クリック数']
    print(number_click)
    #number_click.plot(title='Weekly Clicks')
    #plt.show()

print(kx_click)
