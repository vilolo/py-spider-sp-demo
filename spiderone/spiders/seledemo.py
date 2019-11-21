# -*- coding: utf-8 -*-
import scrapy

from selenium import webdriver


class SeledemoSpider(scrapy.Spider):
    name = 'seledemo'
    allowed_domains = ['www.58pic.com']
    start_urls = ['http://www.58pic.com/']

    # search_page_url_pattern = "https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&page={page}&enc=utf-8"
    # start_urls = ['https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8']

    custom_settings = {
        'DOWNLOADER_MIDDLEWARES' : {'spiderone.middlewares.SeleniumMiddleware': 543,}
    }

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')   #关闭则不提供界面
        chrome_options.add_argument('--no-sandbox') #非沙盘模式
        self.browser = webdriver.Chrome(chrome_options=chrome_options, executable_path='E:\\work_data\\soft src\\chromedriver_win32_76.0.3809.68\\chromedriver.exe')
        super(SeledemoSpider, self).__init__()
    def closed(self,reason):
        self.browser.close()        # 记得关闭

    def parse(self, response):
        print(" into SeledemoSpider ")
        
        pass
