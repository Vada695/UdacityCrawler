

from scrapy.item import Item, Field


class UcrawlerItem(Item):
    title=Field()
    link=Field()
    about=Field()
    desc=Field()
    level=Field()
