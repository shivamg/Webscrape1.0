from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
from parser import parseToFile

from infibeam.items import InfibeamItem
from infibeam.items import InfibeamProductItem


class InfibeamMainPageSpider(BaseSpider):
    name = "InfibeamMainPage"
    allowed_domains = ["infibeam.com"]

    def start_requests(self):
        urls = [line.strip() for line in open('main page links.txt')]
        for url in urls:
            yield Request(url="http://www.infibeam.com/%s/Search_ajax.action?store=%s&page=1" % (url, url),
                          callback=self.parse)

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        categories = hxs.select('//div[contains(@class,"resultsSummary")]')
        items = []
        item = InfibeamItem()
        item['count'] = categories[0].select('.//div[contains(@style,"line-height")]//text()').extract() or [' ']
        item['link'] = response.url
        items.append(item)

        parseToFile(items, 'main page links count.txt', 'mainPage')


class InfibeamProductsSpider(BaseSpider):
    name = "InfibeamProducts"
    allowed_domains = ["infibeam.com"]
    max_cid = 5000

    def start_requests(self):

        urls = [line.strip() for line in open('main page links count.txt')]
        for url in urls:
            href = url[:url.index(",")]
            count = int(int(url[url.index(",")+1:].replace(',',''))/20)
            maxCount = min(self.max_cid, count)
            for i in range(1, maxCount):
                url = href+("%i" % i)
                yield Request(url=url, callback=self.parse)


    def parse(self, response):

        hxs = HtmlXPathSelector(response)

        products = hxs.select('//ul[contains(@class,"srch_result default")]/li')
        items = []
        for product in products:
            item = InfibeamProductItem()
            item['name'] = product.select('.//a/@title').extract()
            item['price'] = product.select('.//span[contains(@class,"normal")]/text()').extract()
            item['image'] = product.select('.//a/img/@src').extract()
            item['link'] = product.select('.//a/@href').extract()
            items.append(item)

        parseToFile(items,'all products.txt','productPage')

