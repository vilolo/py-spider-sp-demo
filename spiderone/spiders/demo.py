# -*- coding: utf-8 -*-
import scrapy

# 这里使用 import 或是 下面from 的方式都行，关键要看 当前项目在pycharm的打开方式，是否是作为一个项目打开的，建议使用这一种方式。
import spiderone.items as items

# 使用from 这种方式，AdilCrawler 需要作为一个项目打开。
# from spiderone.items import AdilcrawlerItem

# 导入 ItemLoader 功能类
from scrapy.loader import ItemLoader


class DemoSpider(scrapy.Spider):
    name = 'demo'
    allowed_domains = ['www.58pic.com/']
    start_urls = ['http://www.58pic.com/c/']
    custom_settings = {
        'ITEM_PIPELINES' : {'spiderone.pipelines.SpideronePipeline1': 300,}
    }

    def parse(self, response):
        # 使用功能类 itemLoader,以取代 看起来杂乱的 extract() 和 xpath() ，优化如下
        i = ItemLoader(item=items.SpideroneItem(), response=response)
        # author 作者
        # theme  主题
        i.add_xpath('author','/html/body/div[5]/div[3]/div/a/p[2]/span/span[2]/text()')
        i.add_xpath('theme','/html/body/div[5]/div[3]/div/a/p[1]/span[1]/text()')
        return i.load_item()


    def parse_old2(self, response):
        item = items.SpideroneItem()

        # author 作者
        # theme  主题

        author = response.xpath('/html/body/div[5]/div[3]/div/a/p[2]/span/span[2]/text()').extract()

        theme = response.xpath('/html/body/div[5]/div[3]/div/a/p[1]/span[1]/text()').extract()

        item['author'] = author
        item['theme']  = theme

        return item


    def parse_old1(self, response):
        '''
        查看页面元素
         /html/body/div[4]/div[3]/div/a/p[2]/span/span[2]/text()
          因为页面中 有多张图，而图是以 /html/body/div[4]/div[3]/div[i]  其中i  为变量 作为区分的 ，所以为了获取当前页面所有的图
          这里 不写 i 程序会遍历 该 路径下的所有 图片。
        '''
        # author 作者
        # theme  主题

        author = response.xpath('/html/body/div[5]/div[3]/div/a/p[2]/span/span[2]/text()').extract()
        theme = response.xpath('/html/body/div[5]/div[3]/div/a/p[1]/span[1]/text()').extract()

        # 使用 爬虫的log 方法在控制台输出爬取的内容。
        self.log(author)
        self.log(theme)

        # 使用遍历的方式 打印出 爬取的内容，因为当前一页有20张图片。
        for i in range(1, 21):
            print(i,' **** ',theme[i - 1], ': ',author[i - 1] )
