from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

import sys
# Add the ptdraft folder path to the sys.path list
sys.path.append('/PycharmProjects/Webscrape1.0/tutorial/')


from tutorial.items import DmozItem

class DmozSpider(BaseSpider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    ]

    def parse(self, response):
       hxs = HtmlXPathSelector(response)
       sites = hxs.select('//ul/li')
       items = []
       for site in sites:
           item = DmozItem()
           item['title'] = site.select('a/text()').extract()
           item['link'] = site.select('a/@href').extract()
           item['desc'] = site.select('text()').extract()
           items.append(item)


       filename = "tutorial links.txt"
       with open(filename, 'wb') as f:
        for item in items:

            #f.write(str(item['title']).strip())
            #f.write(",")
            f.write(str(item['link']).strip())
            #f.write(",")
            #f.write(str(item['desc']).strip())
            f.write("\n")
       f.closed()

