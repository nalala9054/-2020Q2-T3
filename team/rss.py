import feedparser
import json
import bs4
from collections import Counter


def Res():
    urlList = [
        "https://news.google.com/rss/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFZxYUdjU0FtVnVHZ0pWVXlnQVAB/sections/CAQiRENCQVNMUW9JTDIwdk1EVnFhR2NTQW1WdUdnSlZVeUlQQ0FRYUN3b0pMMjB2TURsak4zY3dLZ2dLQmhJRVZTNVRMaWdBKioIAComCAoiIENCQVNFZ29JTDIwdk1EVnFhR2NTQW1WdUdnSlZVeWdBUAFQAQ?hl=en-US&gl=US&ceid=US:en",
        "https://news.google.com/rss/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFZxYUdjU0FtVnVHZ0pWVXlnQVAB/sections/CAQiRENCQVNMUW9JTDIwdk1EVnFhR2NTQW1WdUdnSlZVeUlPQ0FRYUNnb0lMMjB2TURsdWJWOHFDUW9IRWdWWGIzSnNaQ2dBKioIAComCAoiIENCQVNFZ29JTDIwdk1EVnFhR2NTQW1WdUdnSlZVeWdBUAFQAQ?hl=en-US&gl=US&ceid=US:en",
        "https://news.google.com/rss/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFZxYUdjU0FtVnVHZ0pWVXlnQVAB/sections/CAQiSENCQVNNQW9JTDIwdk1EVnFhR2NTQW1WdUdnSlZVeUlPQ0FRYUNnb0lMMjB2TURsek1XWXFEQW9LRWdoQ2RYTnBibVZ6Y3lnQSoqCAAqJggKIiBDQkFTRWdvSUwyMHZNRFZxYUdjU0FtVnVHZ0pWVXlnQVABUAE?hl=en-US&gl=US&ceid=US:en",
        "https://news.google.com/rss/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFZxYUdjU0FtVnVHZ0pWVXlnQVAB/sections/CAQiS0NCQVNNZ29JTDIwdk1EVnFhR2NTQW1WdUdnSlZVeUlPQ0FRYUNnb0lMMjB2TURkak1YWXFEZ29NRWdwVVpXTm9ibTlzYjJkNUtBQSoqCAAqJggKIiBDQkFTRWdvSUwyMHZNRFZxYUdjU0FtVnVHZ0pWVXlnQVABUAE?hl=en-US&gl=US&ceid=US:en",
        "https://news.google.com/rss/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFZxYUdjU0FtVnVHZ0pWVXlnQVAB/sections/CAQiR0NCQVNMd29JTDIwdk1EVnFhR2NTQW1WdUdnSlZVeUlPQ0FRYUNnb0lMMjB2TURadGNUY3FDd29KRWdkVFkybGxibU5sS0FBKioIAComCAoiIENCQVNFZ29JTDIwdk1EVnFhR2NTQW1WdUdnSlZVeWdBUAFQAQ?hl=en-US&gl=US&ceid=US:en",
        "https://news.google.com/rss/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFZxYUdjU0FtVnVHZ0pWVXlnQVAB/sections/CAQiRkNCQVNMZ29JTDIwdk1EVnFhR2NTQW1WdUdnSlZVeUlPQ0FRYUNnb0lMMjB2TUd0ME5URXFDZ29JRWdaSVpXRnNkR2dvQUEqKggAKiYICiIgQ0JBU0Vnb0lMMjB2TURWcWFHY1NBbVZ1R2dKVlV5Z0FQAVAB?hl=en-US&gl=US&ceid=US:en"
        ]
    catList = ["U.S.", "World", "Business", "Technology", "Science", "Health"]
    List_wc = ""
    for i in range(6):
        List_json = []
        d = feedparser.parse(urlList[i])
        for art in d.entries:
            des = []
            root = bs4.BeautifulSoup(art.summary, "lxml")
            dd = root.find_all('a')
            for te in dd:
                if "View Full Coverage on Google News" not in te.text:
                    des.append(te.text)
            data = {
                "source": art.source.title,
                "title": art.title.replace(art.source.title, '').replace(' -',''),
                "url": art.link,
                "date": art.published,
                "description": des
            }
            List_json.append(data)
            List_wc = List_wc + art.title.replace(art.source.title, '').replace(' -','') + '\n'
        with open('googlejson/google_%s.json' % catList[i], 'w') as file:
            json.dump(List_json, file)
        with open('txtfile/for_wc.txt', 'w', encoding="utf-8") as wc:
            wc.write(List_wc)

def clear():
    lines = []
    with open('txtfile/stopwords_en.txt') as f:
        lines = [line.rstrip() for line in f]
    myList = []
    mainstring = " "
    with open('txtfile/for_wc.txt', 'r', encoding='utf-8') as xt:
        every = xt.readlines()
    for i in every:
        mainstring += i.replace(' \n','')
    myDict = Counter(mainstring.split())
    for k, v in myDict.items():
        if k.lower() not in lines and k.isalpha():
            myList.append((k, v))
    myList.sort(key=lambda x: x[1], reverse=True)
    print(myList)

clear()