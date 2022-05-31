# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NadlanscraperItem(scrapy.Item):
    address = scrapy.Field()
    area = scrapy.Field()
    date = scrapy.Field()
    numOfRooms = scrapy.Field()
    size = scrapy.Field()
    floor = scrapy.Field()
    price = scrapy.Field()
    pricePerMeter = scrapy.Field()
    buildYear = scrapy.Field()
    pass
