import pandas as pd
import openpyxl
import datetime

pd.set_option("display.max.columns", 20)


#週データ読み込み
df = pd.read_excel('/Users/Ken/Downloads/マネートラック成果リスト_20210401065006.xlsx', engine='openpyxl')
#リード報酬を消すために、数量0の行を削除
df = df[df['数量'] != 0]
#Correction報酬を削除
df = df[df['商品名']!= 'Correction 報酬調整']

#日付を分割してデータフレームにする（https://note.nkmk.me/python-pandas-split-extract/
trans_datetime = df['日付'].str.split(' ', expand=True)
#インデックスを指定
trans_datetime.columns = ['日付','時間']
#時間の列を削除
trans_date = trans_datetime.drop('時間', axis=1)
#日付の置き換え
df['日付'] = trans_date

#いらない列リスト化
iranai = ['タイプ','2ティアID','2ティア報酬','2ティア報酬','ステータス','支払い状況','最後にクリックされた時間','最後のリファラ','最後のクリックIP','最初のクリック発生時間','最初のクリックIP','ステータス変更日','メモ','請求日','OS']
#.dropで削除
df = df.drop(iranai,axis=1)
#既存CSVファイルに追記 https://note.nkmk.me/python-pandas-to-csv/
df.to_csv('/Users/Ken/Documents/Kiryoku/BK.csv') #, mode='a', header=False
"""

bk = pd.read_csv('/Users/Ken/Documents/Kiryoku/BK.csv', encoding="utf_8_sig", index_col=0)
kx = pd.read_csv('/Users/Ken/Documents/Kiryoku/KX.csv', encoding="utf_8_sig", index_col=0)
pk = pd.read_csv('/Users/Ken/Documents/Kiryoku/PK.csv', encoding="utf_8_sig", index_col=0)
ud = pd.read_csv('/Users/Ken/Documents/Kiryoku/UD.csv', encoding="utf_8_sig", index_col=0)

kiryoku = [bk,kx,pk,ud]
bk_af = ['bpr530','petabout1111','tsukanobu8181','kusuri0121','nobuhisa0427','253674','express','vrh3210','boxpopn','osusume','bbsfvg','addslink','kirara','oimokyo','success8','huangmu136','yuhatasu','Yosuke777','sudir347325','fast4744']
kx_af = ['addslink','easter','bpr530','nobuhisa0427','pcorder','express','sudir347325','tsukanobu8181','keisuke','kusuri0121','tysn23','tuma777','ankerlink','huangmu136','chapy3','motskt','docomo','hiroshi','bbsfvg','vrh3210']
ppc_bk = ['253674','anastacia','daikou','sudir347325','keisuke','osusume','kusuri0622','anastacia','anastacia']
youtube = ['oimokyo','okawarichang123','Etsumi37','shin3maniaTV','okayuvlogs','21461030kyouta','Chappie','takitaki20','hageeta','richestherich','nekurando','ekubo441','otokonobond','sakuraarashi01','taroageage','hiro0204','annabiishiki','tkpablow','y0shiha','mschannel','tamahina','MaybeOfficial','12Yuka18','yuino12','momomo1572','kiki0707ruka','takuma','Sikakkyi','neko18taiki']


#アフィリエイターごと
for af in bk_af:
    df = bk[bk['アフィリエイトID']==af]
    df.to_csv('/Users/Ken/Documents/Kiryoku/BK/'+af+'.csv')

for af in kx_af:
    df = kx[kx['アフィリエイトID']==af]
    df.to_csv('/Users/Ken/Documents/Kiryoku/KX/'+af+'.csv')

for af in ppc_bk:
    df = bk[bk['アフィリエイトID']==af]
    df.to_csv('/Users/Ken/Documents/Kiryoku/BK/ppc_sales.csv')


#商品別各月の売上数量
kiryoku = [bk,kx,pk,ud]
def all_items(site):
    items = site
    items['日付'] = pd.to_datetime(items['日付'])
    items['日付'] = items['日付'].dt.strftime('%Y-%m')
    items2 = pd.pivot_table(items, index = '商品名', columns='日付',values='数量', aggfunc='sum')
    items2.to_excel('/Users/Ken/Downloads/monthly.xlsx',encoding="utf_8_sig")

def monthly_sales(site):
    items = site
    items['日付'] = pd.to_datetime(items['日付'])
    items['日付'] = items['日付'].dt.strftime('%Y-%m')
    items2 = pd.pivot_table(items, columns='日付',values='報酬', aggfunc='sum')
    print(items2)
    #items2.to_excel('/Users/Ken/Downloads/monthly.xlsx',encoding="utf_8_sig")
"""



#商品ごとに数量を集計
#ptl = pd.pivot_table(df, index = '商品名', values='数量', aggfunc='sum')

#df3 = pd.merge(df,df2, on='商品名', how='outer')

#df3.to_csv('/Users/Ken/Downloads/KX5.csv')
