# -*- coding: utf-8 -*-
import scrapy
import spiderone.items
from selenium import webdriver
import time
import sys


class BuckSpider(scrapy.Spider):
    name = 'buck'
    allowed_domains = ['shopee.com.my']
    start_urls = []

    custom_settings = {
        'DOWNLOADER_MIDDLEWARES' : {'spiderone.middlewares.SeleniumMiddleware': 543,},
        'ITEM_PIPELINES' : {'spiderone.pipelines.BuckPipeline': 300,}
    }

    def __init__(self, name=None, **kwargs):
        super().__init__(name=name, **kwargs)
        chrome_options = webdriver.ChromeOptions()
        #chrome_options.add_argument('--headless')   #关闭则不提供界面
        #chrome_options.add_argument('--no-sandbox') #非沙盘模式
        self.browser = webdriver.Chrome(chrome_options=chrome_options, executable_path='E:\\work_data\\soft src\\chromedriver_win32_76.0.3809.68\\chromedriver.exe')

        self.start_urls.append('https://shopee.com.my/sinewing.my')

        self.crawlid = int(time.time())

        self.curPage = 0
        

    def closed(self,reason):
        self.browser.close()        # 记得关闭

    def parse(self, response):
        # name = scrapy.Field()
        # storeId = scrapy.Field()
        # products = scrapy.Field()
        # joined = scrapy.Field()
        # followers = scrapy.Field()
        # following = scrapy.Field()
        # rating = scrapy.Field()
        item = spiderone.items.buckStoreItem()

        name = response.css('.section-seller-overview-horizontal__portrait-name::text').extract()[0]
        storeId = response.css('.navbar-with-more-menu__item:nth-child(2)::attr("href")').re(r'\d+')[0]

        value_list = response.css('.section-seller-overview__item-text-value::text').extract()
        products = value_list[0]
        joined = value_list[13]
        followers = value_list[9]
        following = value_list[5]
        rating = value_list[11]

        item['name'] = name
        item['storeId'] = storeId
        item['products'] = products
        item['joined'] = joined
        item['followers'] = followers
        item['following'] = following
        item['rating'] = rating
        item['crawlid'] = self.crawlid

        print('============res=============')
        #print(item)
        print('============end=============')

        yield item

        productPage = response.css('.navbar-with-more-menu__item:nth-child(2)::attr("href")').extract()
        yield scrapy.Request(url=productPage, callable=self.parse_detail)

    def parse_detail(self, response):
        i = scrapy.loader.Itemloader(item=spiderone.items.buckProductItem, response=response)