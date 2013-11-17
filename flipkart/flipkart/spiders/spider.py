from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request

from parser import parseToFile
from flipkart.items import FlipkartItem
from flipkart.items import FlipkartProductItem


class FlipkartMainPageSpider(BaseSpider):
    name = "FlipkartMainPage"
    allowed_domains = ["flipkart.com"]

    def start_requests(self):
        urls = [line.strip() for line in open('main page links.txt')]
        for url in urls:
            yield Request(url="http://www.flipkart.com" + url, callback=self.parse)

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        count = hxs.select('//span[contains(@class,"items")]/text()').extract()
        items = []
        item = FlipkartItem()
        item['count'] = count
        item['link'] = response.url
        items.append(item)
        #filename should be a config file input
        parseToFile(items, 'main page links count.txt', 'mainPage')


class FlipkartProductsSpider(BaseSpider):
    name = "FlipkartProducts"
    allowed_domains = ["flipkart.com"]
    #config file input
    max_cid = 5
    download_delay = 2

    def start_requests(self):
        urls = [line.strip() for line in open('main page links count.txt')]
        for url in urls:
            href = url[:url.index(",")]
            #count = int(int(url[url.index(",")+1:])/20)
            #maxCount = min(self.max_cid, count)
            #for i in range(1, maxCount):
            url = href+("&start=20&ajax=true")
            yield Request(url=url, callback=self.parse)

    def parse(self, response):
        if response.status == 200:
            hxs = HtmlXPathSelector(response)
            products = hxs.select('//textarea')
            items = []
            for product in products:
                item = FlipkartProductItem()
                item['text'] = product.extract()
                items.append(item)
                #filename to be read from config file
            parseToFile(items, 'all products.txt', 'productPage')
            url = response.url
            urlIterator = int(url[url.index("&start=")+7:url.index("&ajax=")])+20
            url = url[:url.index("&start=")] + "&start=" + str(urlIterator) + "&ajax=true"
            if urlIterator < 60:
                yield Request(url=url, callback=self.parse)

