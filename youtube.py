from apiclient.discovery import build
import pandas as pd
import openpyxl
import requests
import json
import slackweb
from datetime import date, datetime, timedelta


API_KEY = 'AIzaSyCNnnsZsFCMWZI7etcpCFWk5m0Q03DtRfM'
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'
SEARCH_TEXT = 'ピル'

youtube = build(
YOUTUBE_API_SERVICE_NAME,
YOUTUBE_API_VERSION,
developerKey=API_KEY
)

slack = slackweb.Slack(url='https://hooks.slack.com/services/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')

yesterday =str(date.today()-timedelta(days=1))
today = str(date.today())


def get_video_info(q,num):
    search_response = youtube.search().list(
    part='snippet',
    #検索ワード
    q=q,
    #ソート
    order='date',
    type='video',
    maxResults=num,
    publishedBefore=today+"T00:00:00Z",
    publishedAfter=yesterday+"T00:00:00Z"
    ).execute()
    slack.notify(text="お疲れさまです。こちらのYoutubeの勧誘お願いいたします。")
    for sr in search_response.get('items',[]):
        date = sr['snippet']['publishedAt']
        channel_name = sr['snippet']['channelTitle']
        channel_title = sr['snippet']['title']
        description = sr['snippet']['description']
        video_id = sr['id']['videoId']
        url = 'https://www.youtube.com/watch?v='+video_id
        info = '日付：'+date+'\n'+'チャンネル名：'+channel_name+'\n'+'URL：'+url
        slack.notify(text=info)
        slack.notify(text=date)
        slack.notify(text=channel_name)
        slack.notify(text=channel_title)
        slack.notify(text=description)
        slack.notify(text=url)
        slack.notify(text='-------------------------')

get_video_info(q='ピル',num=5)



#https://qiita.com/taka-kawa/items/f0597b2f375da7ddbb73
#https://developers.wonderpla.net/entry/2020/06/18/110005
#https://qiita.com/g-k/items/7c98efe21257afac70e9


"""
#numに入れた数字x5健の情報を取得
#その他のパラメータはAPIから情報を取得するパラメータと同じ
def get_video_info(part, q, order, type, num):
    dic_list = []
    search_response = youtube.search().list(part=part, q=q, order=order, type=type, maxResults=num)
    output = search_response.execute()

    for i in range(num):
        dic_list = dic_list + output['items']
        search_response = youtube.search().list_next(search_response, output)
        output = search_response.execute()

        df = pd.DataFrame(dic_list)

        #video_id = df['videoId']
        df1 = pd.DataFrame(list(df['id']))['videoId']
        df2 = pd.DataFrame(list(df['snippet']))[['channelTitle', 'publishedAt','channelId','title', 'description']]

        ddf = pd.concat([df1, df2], axis = 1)

        return ddf


op = get_video_info(part='snippet', q='スキンケア', order='date', type = 'video', num = 20)
op.to_excel('/Users/Ken/*.xlsx', sheet_name='11')
"""
#https://note.nkmk.me/python-pandas-to-excel/
