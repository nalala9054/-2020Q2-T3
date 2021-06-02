import json
import craw_url as cu
import datetime

starttime = datetime.datetime.now()

with open("json/news.json",'r+', encoding='UTF-8') as f:
    params = json.load(f)
with open ('json/news_content.json','w', encoding='UTF-8') as hello:
    for i in range(len(params['articles'])):
        try:
            cu.classify(params['articles'][i]['url'])
            with open('tttt.txt', 'r', encoding='UTF-8') as file:
                data = file.read()
            params['articles'][i]['content'] = data
        except AttributeError:
            pass
        except TypeError:
            pass
    json.dump(params, hello)

endtime = datetime.datetime.now()
print (endtime - starttime)
