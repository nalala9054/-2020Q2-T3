import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import numpy as np #繪製mask圖形
from PIL import Image
import json

def cloud(image, text, max_word, max_font, random):
    stopwords = set(STOPWORDS)
    stopwords.update(['us', 'one', 'will', 'said', 'now', 'well', 'man', 'may',
    'little', 'say', 'must', 'way', 'long', 'yet', 'mean',
    'put', 'seem', 'asked', 'made', 'half', 'much',
    'certainly', 'might', 'came', 'definition', 'S'])


    wc = WordCloud(
    background_color="white",
    colormap="hot",
    max_words=max_word,
    mask=image,
    stopwords=stopwords,
    max_font_size=max_font,
    random_state=random
    )
    # generate word cloud
    wc.generate(text)

    # create coloring from image
    image_colors = ImageColorGenerator(image)

    # 畫圖
    plt.figure(figsize=(200,200))
    plt.imshow(wc, interpolation="bilinear")
    wc.to_file('output/wordcloud.png')
    '''
    若要產生原圖比對
    fig, axes = plt.subplots(1,2, gridspec_kw={'width_ratios': [3, 2]})
    axes[0].imshow(wc, interpolation="bilinear")
    axes[1].imshow(image, cmap=plt.cm.gray, interpolation="bilinear")
    for ax in axes:
        ax.set_axis_off()

    fig.savefig('./images/ESG_WordCloud.png')
    '''
    #頻率表
    freqList  = wc.process_text(text)
    freqList = sorted(freqList.items(), key=lambda x:x[1])
    freqList.reverse()
    with open('txtfile/freqList.txt', 'w', encoding='UTF-8') as obj:
        json.dump(freqList, obj)

text = open('txtfile/for_wc.txt','r',encoding='UTF-8', errors='ignore').read()
mask = np.array(Image.open("images/circle.png"))
cloud(mask,text,200,60,42)
