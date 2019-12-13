# -*- coding: utf-8 -*-
import scrapy
import spiderone
from selenium import webdriver

class SpdemoSpider(scrapy.Spider):
    name = 'spdemo'
    allowed_domains = ['shopee.com.my']
    start_urls = ['https://shopee.com.my/shop/178840654/search?page=0&sortBy=relevancy']

    custom_settings = {
        'DOWNLOADER_MIDDLEWARES' : {'spiderone.middlewares.SeleniumMiddleware': 543,}
    }

    cur_page = 0

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        #chrome_options.add_argument('--headless')   #关闭则不提供界面
        #chrome_options.add_argument('--no-sandbox') #非沙盘模式
        self.browser = webdriver.Chrome(chrome_options=chrome_options, executable_path='E:\\work_data\\soft src\\chromedriver_win32_76.0.3809.68\\chromedriver.exe')
        super(SpdemoSpider, self).__init__()
    def closed(self,reason):
        self.browser.close()        # 记得关闭

    def parse(self, response):
        i = scrapy.loader.ItemLoader(item=spiderone.items.spDemoItem(), response=response)

        i.add_css('name', '.shopee-seller-portrait__name::text')
        i.add_css('plist', '.shop-search-result-view__item a::attr(href)')

        info = i.load_item()
        print("============================================="+str(self.cur_page))
        print(info['name'])
        yield info

        print("***************************")

        self.cur_page = self.cur_page + 1
        yield scrapy.Request(url='https://shopee.com.my/shop/71665063/search?page='+str(self.cur_page)+'&sortBy=sales', callback=self.parse_detail, meta={'data':self.cur_page})

    
    def parse_detail(self,response):
        i = scrapy.loader.ItemLoader(item=spiderone.items.spDemoItem(), response=response)

        i.add_css('name', '.shopee-seller-portrait__name::text')
        i.add_css('plist', '.shop-search-result-view__item a::attr(href)')

        info = i.load_item()
        print("============================================="+str(self.cur_page))
        print(info['name'])

        if 'plist' not in info.keys():
            return

        yield info

        self.cur_page = self.cur_page + 1
        yield scrapy.Request(url='https://shopee.com.my/shop/71665063/search?page='+str(self.cur_page)+'&sortBy=sales', callback=self.parse_detail, meta={'data':self.cur_page})


