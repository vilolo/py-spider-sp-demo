# -*- coding: utf-8 -*-
import scrapy

import spiderone.items

#from scrapy.loader import ItemLoader

class MysqldemoSpider(scrapy.Spider):
    name = 'mysqldemo'
    allowed_domains = ['www.58pic.com/']
    start_urls = ['http://www.58pic.com/c/']

    def parse(self, response):
        print(" ===================into  MysqldemoSpider======================= ")

        # i = scrapy.loader.ItemLoader(item=spiderone.items.mysqlDemoItem(), response=response)

        # #i.add_css('img', 'img::attr(src)')
        # i.add_css('img', '.wrap-list')
        # info = i.load_item()
        

        #=========== 获取节点，再循环分析 ====================
        # print(len(info.get('img')))
        # print(type(info))

        # for str in info.get('img'):
        #     t = str.css('a::attr(href)').extract()
        #     print(t)

        # #print(f"articleInfo = {info}")
        # print("***********************")

        # l = response.css(".wrap-list")

        # for ll in l:
        #     href = ll.css("a::attr(href)").extract()
        #     print(href[0])

        #=========== 解析字符串 html ====================
        html = "<div><a href='xxx.com'>wahahahah</a></div>"
        str = scrapy.selector.Selector(text=html).xpath("//div/a/text()").extract()
        print(str[0])


