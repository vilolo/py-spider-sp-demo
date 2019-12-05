# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SpideroneItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    author = scrapy.Field()
    theme = scrapy.Field()

class mysqlDemoItem(scrapy.Item):
    img = scrapy.Field()
    title = scrapy.Field()
    desc = scrapy.Field()

class spDemoItem(scrapy.Item):
    name = scrapy.Field()
    pnum = scrapy.Field()
    plist = scrapy.Field()