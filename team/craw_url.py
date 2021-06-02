import urllib.request as req
import bs4


def catch_r_article(url):
    request_reuters = req.Request(url, headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"})
    with req.urlopen(request_reuters) as response:
        data_reuters = response.read()
    root_reuters = bs4.BeautifulSoup(data_reuters, "html.parser")
    title_reuters = root_reuters.find_all("h1", class_="Headline-headline-2FXIq Headline-black-OogpV ArticleHeader-headline-NlAqj")
    content_reuters = root_reuters.find_all("p", class_="Paragraph-paragraph-2Bgue ArticleBody-para-TD_9x")

    if content_reuters == []:
        content_reuters = root_reuters.find_all("p", class_="Text__text___3eVx1j Text__dark-grey___AS2I_p Text__regular___Bh17t- Text__large___1i0u1F Body__base___25kqPt Body__large_body___3g04wK ArticleBody__element___3UrnEs")

    with open("tttt.txt", "w", encoding="utf-8") as file:  # "w":覆寫，"a":附加寫入
        '''
        file.write("sources : reuters\n")
        file.write(title_reuters[0].string + "\n")
        file.write("content : \n")
        '''
        for tag in content_reuters:
            if tag.string !=None:
                if "=====" not in tag.string:
                    file.write(tag.string + '\n')



def catch_r_tech(url):
    if "reuters.com" in url:
        request_reuters = req.Request(url, headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"})
    with req.urlopen(request_reuters) as response:
        data_reuters = response.read()
    root_reuters = bs4.BeautifulSoup(data_reuters, "html.parser")
    title_reuters = root_reuters.find_all("h1", class_="Text__text___3eVx1j Text__dark-grey___AS2I_p Text__medium___1ocDap Text__heading_2___sUlNJP Heading__base___1dDlXY Heading__heading_2___3f_bIW")
    content_reuters = root_reuters.find_all("p", class_="Text__text___3eVx1j Text__dark-grey___AS2I_p Text__regular___Bh17t- Text__large___1i0u1F Body__base___25kqPt Body__large_body___3g04wK ArticleBody__element___3UrnEs")

    with open("tttt.txt", "w", encoding="utf-8") as file:
        '''
        file.write("sources : reuters\n")
        file.write(title_reuters[0].string + "\n")
        file.write("content : \n")
        '''
        for tag in content_reuters:
            if tag.string !=None:
                file.write(tag.string + '\n')

def catch_BI(url):
    request_BI = req.Request(url, headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"})
    with req.urlopen(request_BI) as response:
        data_BI = response.read()
    root_BI = bs4.BeautifulSoup(data_BI, "html.parser")
    title_BI = root_BI.find("h1", class_="article-title")
    content_BI = root_BI.find("div", class_="col-xs-12 news-content no-padding")

    if content_BI == None:
        content_BI = root_BI.find("div", class_="content-lock-content")


    with open("tttt.txt", "w", encoding="utf-8") as file:
        '''
        file.write("sources : business insider\n")
        file.write(title_BI.string + "\n")
        file.write("content : \n")
        '''
        for tag in content_BI.find_all('p'):
            if tag.find('span'):
                continue
            if tag.get('class'):
                continue
            if tag.find('em'):
                continue
            if tag.text != None:
                file.write(tag.text + '\n')
        for tag in content_BI.find_all('li'):
            if tag.text != None:
                if "Sign up" not in tag.text:
                    if "Pros" not in tag.text:
                        if "Details" not in tag.text:
                            file.write(tag.text + '\n')


def catch_bloomberg(url):
    if "www.bloomberg.com" in url:
        request = req.Request(url, headers={
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
            })
    with req.urlopen(request) as response:
        data = response.read()
    root = bs4.BeautifulSoup(data, "html.parser")
    print(root)
    content = root.find("div", class_="body-columns")

    with open("tttt.txt", "w", encoding="utf-8") as file:
        '''
        file.write("sources : bloomberg\n")
        file.write(title.find('h1').text + "\n")
        file.write("content : \n")
        '''
        for i in content.find_all('p'):
            if i.find('span'):
                continue
            if i.text != None:
                if "Sign up" not in i.text:
                    if "Read more" not in i.text:
                        if "*" not in i.text:
                            if "Data:" not in i.text:
                                if "LISTEN:" not in i.text:
                                    if "— With" not in i.text:
                                        file.write(i.text + '\n')
        for j in content.find_all('h2'):
            if j.text != None:
                if "SHARE THIS ARTICLE" not in j.text:
                    if "LISTEN TO" not in j.text:
                        file.write(j.text +'\n')


def catch_fin_post(url):
    request = req.Request(url, headers={"user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"})
    with req.urlopen(request) as response:
        data = response.read()
    root = bs4.BeautifulSoup(data, "html.parser")
    title = root.find("h1", class_="article-title")
    content = root.find_all("section", class_="article-content__content-group")

    with open("tttt.txt", "w", encoding="utf-8") as file:
        '''
        file.write("sources : financil-post\n")
        file.write(title.string + "\n")
        file.write("content : \n")
        '''
        for section in content:
            for i in section.find_all('p'):
                if i.find('em'):
                    continue
                if i.text != None:
                    if "_____________________________________________________________" not in i.text:
                        file.write(i.text + '\n')
            for j in section.find_all('h2'):
                if j.text != None :
                    if 'Article content' not in j.text:
                        if 'More On This Topic' not in j.text:
                            file.write(i.text+'\n')


def classify(url):
    if "reuters.com/article" in url:
        catch_r_article(url)
    if "reuters.com/technology" in url:
        catch_r_tech(url)
    if "www.reuters.com/world" in url:
        catch_r_tech(url)
    if "www.reuters.com" in url:
        catch_r_article(url)
    if "businessinsider.com" in url:
        catch_BI(url)
    if "www.bloomberg.com" in url:
        catch_bloomberg(url)
    if "financialpost.com" in url:
        catch_fin_post(url)






url = "https://www.bloomberg.com/news/articles/2021-05-28/giuliani-raid-materials-will-get-outside-review-judge-rules"
classify(url)