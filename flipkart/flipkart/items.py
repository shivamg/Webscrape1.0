# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class FlipkartItem(Item):
    # define the fields for your item here like:
    count = Field()
    link = Field()


class FlipkartProductItem(Item):
    # define the fields for your item here like:
    # name = Field()
    text = Field()

