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

class buckStoreItem(scrapy.Item):
    crawlid = scrapy.Field()
    name = scrapy.Field()
    storeId = scrapy.Field()
    products = scrapy.Field()
    joined = scrapy.Field()
    followers = scrapy.Field()
    following = scrapy.Field()
    rating = scrapy.Field()

class buckProductItem(scrapy.Item):
    crawlid = scrapy.Field()
    pcode = scrapy.Field()
    cover = scrapy.Field()
    discount = scrapy.Field()
    activity = scrapy.Field()
    multipleOffer = scrapy.Field()
    title = scrapy.Field()
    price = scrapy.Field()
    likes = scrapy.Field()
    sales = scrapy.Field()
    categorys = scrapy.Field()
    popularRanking = scrapy.Field()
    url = scrapy.Field()

