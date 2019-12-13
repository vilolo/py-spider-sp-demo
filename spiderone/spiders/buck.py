# -*- coding: utf-8 -*-
import scrapy
import spiderone.items
from selenium import webdriver
import time
import sys
from scrapy.http.response.html import HtmlResponse
from spiderone.items import buckProductItem
from time import sleep


class BuckSpider(scrapy.Spider):
    name = 'buck'
    allowed_domains = ['shopee.com.my']
    start_urls = []
    cur_page = 1

    custom_settings = {
        'DOWNLOADER_MIDDLEWARES' : {
            'spiderone.middlewares.SeleniumMiddleware': 543,
            "scrapy.contrib.downloadermiddleware.redirect.RedirectMiddleware": None,
            },
        'ITEM_PIPELINES' : {
            'spiderone.pipelines.BuckPipeline': 300
            },
        'RETRY_ENABLED' : True
    }

    def __init__(self, name=None, **kwargs):
        super().__init__(name=name, **kwargs)
        chrome_options = webdriver.ChromeOptions()
        #chrome_options.add_argument('--headless')   #关闭则不提供界面
        #chrome_options.add_argument('--no-sandbox') #非沙盘模式
        self.browser = webdriver.Chrome(chrome_options=chrome_options, executable_path='E:\\work_data\\soft src\\chromedriver_win32_76.0.3809.68\\chromedriver.exe')

        self.start_urls.append('https://shopee.com.my/swshoeswholesaler')

        self.crawlid = int(time.time())

        self.curPage = -1
        

    def closed(self,reason):
        # self.browser.close()        # 记得关闭
        pass

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

        #print('============res=============')
        #print(item)
        #print('============end=============')

        yield item

        productPage = response.css('.navbar-with-more-menu__item:nth-child(2)::attr("href")').extract()
        
        print('============666=============')
        print(response.urljoin(productPage[0]))
        self.cur_page = self.cur_page + 1
        url = response.urljoin(productPage[0]) + "?page=" + str(self.cur_page)
        
        yield scrapy.Request(url=url, callback=self.productList)

    def productList(self, response):
        # crawlid = scrapy.Field()
        # pcode = scrapy.Field()
        # cover = scrapy.Field()
        # discount = scrapy.Field()
        # activity = scrapy.Field()
        # multipleOffer = scrapy.Field()
        # title = scrapy.Field()
        # price = scrapy.Field()
        # likes = scrapy.Field()
        # sales = scrapy.Field()
        # categorys = scrapy.Field()
        # popularRanking = scrapy.Field()
        # url = scrapy.Field()
        pboxList = response.css(".shop-search-result-view__item")
        print("======== into pboxList ==========");

        for pbox in pboxList:
            pitem = buckProductItem()
            pitem['crawlid'] = self.crawlid
            url = response.urljoin(pbox.css('a::attr(href)').extract()[0])
            pitem['pcode'] = url[url.rfind('.')+1:]
            pitem['cover'] = scrapy.selector.Selector(text=pbox.extract()).xpath('//div/div/a/div/div/div/@style').re(".*\"(.*)\"")[0]
            pitem['discount'] = pbox.css('.percent::text').extract()[0] if pbox.css('.percent::text').extract() else ""
            pitem['activity'] = ''
            pitem['multipleOffer'] = pbox.css('._2B9nvB::text').extract()[0] if pbox.css('._2B9nvB::text').extract() else (pbox.css('._3TvbSB').extract()[0] if pbox.css('._3TvbSB').extract() else "")
            pitem['url'] = url;

            yield pitem;


        



        