import asyncio
from bs4 import BeautifulSoup
import asyncio
from pyppeteer import launch
from pyquery import PyQuery as pq

async def main():
    browser = await launch()
    page = await browser.newPage()
    await page.goto('https://www.bloomberg.com/news/articles/2021-05-28/giuliani-raid-materials-will-get-outside-review-judge-rules')
    doc = pq(await page.content())
    print('Quotes:', doc('.quote').length)
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())
