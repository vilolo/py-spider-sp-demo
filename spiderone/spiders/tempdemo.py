# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.loader import ItemLoader
import spiderone.items as items

class TempdemoSpider(CrawlSpider):
    name = 'tempdemo'
    allowed_domains = ['www.58pic.com']
    # 修改起始页地址
    start_urls = ['http://www.58pic.com/c/']

    custom_settings = {
        'ITEM_PIPELINES' : {'spiderone.pipelines.SpideronePipeline2': 300,}
    }

    # Response里链接的提取规则，返回的符合匹配规则的链接匹配对象的列表
    # http://www.58pic.com/c/1-0-0-03.html  根据翻页连接地址，找到 相应的 正则表达式   1-0-0-03  -> \S-\S-\S-\S\S  而且 这里使用 allow
    # 不能使用 restrict_xpaths ，使用 他的话，正则将失效
    page_link = LinkExtractor(allow='//www.58pic.com/c/\\S-\\S-\\S-\\S\\S.html', allow_domains='www.58pic.com')

    rules = (
        # 获取这个列表里的链接，依次发送请求，并且继续跟进，调用指定回调函数处理
        Rule(page_link, callback='parse_item', follow=True),  # 注意这里的 ',' 要不会报错
    )

    # 加上这个 方法是为了 解决 parse_item() 不能抓取第一页数据的问题 parse_start_url 是 CrawlSpider() 类下的方法，这里重写一下即可
    def parse_start_url(self, response):

        self.log("++++++++++++++++++++++++++++++++++++")
        tt = response.xpath('/html/body/div[5]/div[3]/div/a/p[2]/span/span[2]/text()').extract()
        self.log(tt)
        self.log("++++++++++++++++++++++++++++++++++++")

        i = ItemLoader(item = items.SpideroneItem(),response = response )
        i.add_xpath('author','/html/body/div[5]/div[3]/div/a/p[2]/span/span[2]/text()')
        i.add_xpath('theme','/html/body/div[5]/div[3]/div/a/p[1]/span[1]/text()')

        res = i.load_item()

        print(f"data = {res}")

        yield res

    # 指定的回调函数
    def parse_item(self, response):
        i = ItemLoader(item = items.SpideroneItem(),response = response )
        i.add_xpath('author','/html/body/div[5]/div[3]/div/a/p[2]/span/span[2]/text()')
        i.add_xpath('theme','/html/body/div[5]/div[3]/div/a/p[1]/span[1]/text()')

        res = i.load_item()

        print(f"data = {res}")

        yield res


class TempdemoSpider_old(CrawlSpider):
    name = 'tempdemo_old'
    allowed_domains = ['www.58pic.com']
    start_urls = ['http://www.58pic.com/c/']

    # https://www.58pic.com/c/1-0-0-4.html
    page_link = LinkExtractor(allow='//www.58pic.com/c/\\S-\\S-\\S-\\S.html', allow_domains='www.58pic.com')

    rules = (
        Rule(page_link, callback='parse_item', follow=True),
    )

    # 加上这个 方法是为了 解决 parse_item() 不能抓取第一页数据的问题 parse_start_url 是 CrawlSpider() 类下的方法，这里重写一下即可
    def parse_start_url_old(self, response):
        # 使用功能类 itemLoader,以取代 看起来杂乱的 extract() 和 xpath() ，优化如下
        i = ItemLoader(item=items.SpideroneItem(), response=response)
        # author 作者
        # theme  主题
        i.add_xpath('author','/html/body/div[5]/div[3]/div/a/p[2]/span/span[2]/text()')
        i.add_xpath('theme','/html/body/div[5]/div[3]/div/a/p[1]/span[1]/text()')
        yield i.load_item()


    def parse_item(self, response):
        # 使用功能类 itemLoader,以取代 看起来杂乱的 extract() 和 xpath() ，优化如下
        i = ItemLoader(item=items.SpideroneItem(), response=response)
        # author 作者
        # theme  主题
        i.add_xpath('author','/html/body/div[5]/div[3]/div/a/p[2]/span/span[2]/text()')
        i.add_xpath('theme','/html/body/div[5]/div[3]/div/a/p[1]/span[1]/text()')
        yield i.load_item()