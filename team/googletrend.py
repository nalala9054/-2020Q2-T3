from pytrends.request import TrendReq
import pandas as pd
import json


pytrend = TrendReq(hl='en-US', tz=360)
pytrend.build_payload(kw_list=["MSCI"], timeframe='today 3-m', geo='US', gprop='')
js = pytrend.related_topics()  # 相關話題
js['MSCI']['rising']




pytrends = TrendReq(hl = 'en-US', tz = 360)

# 如果想要知道現在美國地區的人都在搜尋什麼，可以這樣查詢
hd = pytrends.trending_searches(pn = 'united_states')
print(hd)