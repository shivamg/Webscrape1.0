from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request

from parser import parseToFile
from snapdeal.items import SnapdealItem
import json

class snapdealMainPageSpider(BaseSpider):
    name = "SnapdealMainPage"
    allowed_domains = ["snapdeal.com"]

    def start_requests(self):
        urls = [line.strip() for line in open('main page links.txt')]
        for url in urls:
            url = url[:url.index(",")]
            yield Request(url=url, callback=self.parse)

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        count = hxs.select('//span[contains(@id,"no-of-results-filter")]/text()').extract() or ['']
        items = []
        item = SnapdealItem()
        item['count'] = count
        item['link'] = response.url
        items.append(item)
        #filename should be a config file input
        parseToFile(items, 'main page links count.txt', 'mainPage')


class snapdealProductsSpider(BaseSpider):
    name = "SnapdealProducts"
    allowed_domains = ["snapdeal.com"]
    #config file input
    max_cid = 5000

    def start_requests(self):
        urls = [line.strip() for line in open('main page links count.txt')]
        for url in urls:
            href = url[:url.index(",")]
            count = int(int(url[url.index(",")+1:])/20)
            maxCount = min(self.max_cid, count)
            for i in range(1, maxCount):
                url = href+("/%i/20?q=&sort=plrty&keyword=&clickSrc=&viewType=Grid" % (i * 20))
                yield Request(url=url, callback=self.parse)

    def parse(self, response):

        jsonResponse = json.loads(response.body)
        items = jsonResponse['productDtos']
        parseToFile(items, 'all products.txt', 'productPage')
