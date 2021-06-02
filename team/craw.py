from newsapi import NewsApiClient
import json
import datetime as dt
from collections import Counter

apiKey = 'fd3c831a6b564adbab26096caf879f9f'
newsapi = NewsApiClient(api_key=apiKey)
fin_sources="bloomberg,reuters,fortune,business-insider,financial-post,australian-financial-review" #, the-wall-street-journal"
head_sources="CNBC" or "The New York Times" or "The Hill" or "Investor's Business Daily" or "CNN" or " The Wall Street Journal" or "The Associated Press" or "Yahoo Finance" or "Markets Insider" or "MarketWatch" or "NBC News" or "The Verge" or "NPR" or "Fox Business" or "Reuters"
lines = []
with open('txtfile/stopwords_en.txt') as f:
    lines = [line.rstrip() for line in f]


def mutual(keywords): #手動輸入關鍵字，期間為一禮拜
    everything = newsapi.get_everything(
        q=keywords,
        language='en',
        sources=fin_sources,
        from_param = dt.date.today() - dt.timedelta(days = 7),
        to= dt.date.today(),
        page_size= 100,
        page = 1,
        sort_by = 'publishedAt'
        )

    #產生txt檔(for_wc.txt)給文字雲使用
    with open('txtfile/for_wc.txt', 'w', encoding='UTF-8') as f:
        for i in everything["articles"]:
            f.write(i['title']+'')
    #產生json檔
    file = 'news.json'
    with open('json/'+ file, 'w', encoding="utf-8") as f:
        json.dump(everything, f)
    '''
    #資料清洗
    myList = []
    mainstring = " "
    for i in everything["articles"]:
        mainstring += i["title"]
    myDict = Counter(mainstring.split())
    for k, v in myDict.items():
        if k.lower() not in lines and k.isalpha():
            myList.append((k, v))
    myList.sort(key=lambda x: x[1], reverse=True)
    print(myList)
    '''


def auto():
    headlines = newsapi.get_top_headlines(
        country='us',
        category="business",
        page_size= 100,
        page = 1
    )
    #產生txt檔(for_wc.txt)給文字雲使用
    with open('txtfile/for_wc.txt', 'w', encoding='UTF-8') as f:
        for i in headlines["articles"]:
            if  head_sources in i['title']:
                f.write(i['title'].replace(head_sources,'')+'')
            else :
                f.write(i['title'])
    #產生json檔
    file = 'news.json'
    with open('json/'+ file, 'w', encoding="utf-8") as f:
        json.dump(headlines, f)

def pic():
    with open('json/news.json', 'r') as j:
        data = json.load(j)
    for i in data['articles']:
        print(i['urlToImage'])
