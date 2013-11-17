# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html


from scrapy.item import Item, Field

class MyntraItem(Item):
    # define the fields for your item here like:
    link = Field()
    count = Field()

class MyntraProductItem(Item):
    # define the fields for your item here like:
    link = Field()
    name = Field()
    price = Field()
    image = Field()
