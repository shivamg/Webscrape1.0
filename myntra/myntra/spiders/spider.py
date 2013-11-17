

from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request

from parser import parseToFile

from myntra.items import MyntraItem
from myntra.items import MyntraProductItem

class myntraMainPageSpider(BaseSpider):
    name = "MyntraMainPage"
    allowed_domains = ["myntra.com"]

    def start_requests(self):
        urls = [line.strip() for line in open('main page links.txt')]
        for url in urls:
            yield Request(url="http://www.myntra.com"+url, callback=self.parse)

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        count = hxs.select('//div[contains(@class,"mk-product-count")]/text()').extract() or ['']
        items = []
        item = MyntraItem()
        item['count'] = count
        item['link'] = response.url
        items.append(item)
        #filename should be a config file input
        parseToFile(items, 'main page links count.txt', 'mainPage')


class MyntraProductsSpider(BaseSpider):

    name = "MyntraProducts"
    allowed_domains = ["myntra.com"]
    max_cid = 5

    def start_requests(self):
        urls = [line.strip() for line in open('main page links count.txt')]
        for url in urls:
            href = url[:url.index(",")]
            count = int(int(url[url.index(",")+1:])/20)
            maxCount = min(self.max_cid, count)
            for i in range(1, maxCount):
                url = href+("%i" % i)
                yield Request(url=url, callback=self.parse)

    def parse(self, response):

        hxs = HtmlXPathSelector(response)
        products = hxs.select('//a[contains(@style,"display:block")]')
        items = []
        for product in products:
            item = MyntraProductItem()
            item['name'] = product.select('.//span[contains(@class,"mk-prod-name")]/text()').extract()
            item['price'] = product.select('.//span[contains(@class,"mk-prod-price")]/text()').extract()
            item['image'] = product.select('.//img/@src').extract()
            item['link'] = product.select('@href').extract()
            items.append(item)

        parseToFile(items,'all products.txt','productPage')
