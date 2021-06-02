import sys
sys.path.append('C:\\Users\\new\\Desktop\\文字探勘與機器學習\\Python\\team')
from newsapi import NewsApiClient
import json
import datetime as dt
import craw
import wc
import trend
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import numpy as np
from PIL import Image
from fbprophet import Prophet
from pytrends.request import TrendReq




keyword = 'Trump'
craw.mutual(keyword)

text = open('txtfile/for_wc.txt','r',encoding='UTF-8', errors='ignore').read()
mask = np.array(Image.open("images/circle.png"))
wc.cloud(mask,text,200,60,42)

periods=90
df = trend.get_data(keyword)
forecast, fig1, fig2 = trend.make_pred(df, periods)
fig1.savefig('output/trend1.png')
fig2.savefig('output/trend2.png')

