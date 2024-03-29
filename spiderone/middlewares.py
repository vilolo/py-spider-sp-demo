# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

from scrapy.http import HtmlResponse
from selenium import webdriver
import time
from scrapy.utils.response import response_status_message
from scrapy.downloadermiddlewares.retry import RetryMiddleware

class SpideroneSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class SpideroneDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class SeleniumMiddleware(RetryMiddleware):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        spider.browser.get(request.url)
        # for i in range(2):
        #     spider.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        time.sleep(3)


        js = 'var langBtn = document.getElementsByClassName("shopee-button-outline--primary-reverse"); if(langBtn.length > 0){langBtn[0].click();};'
        spider.browser.execute_script(js); 

        # spider.browser.execute_script('setTimeout(window.scrollTo(0, 500), 1000)')
        # spider.browser.execute_script("window.scrollTo(500, 700);")
        # spider.browser.execute_script("alert('123');")
        spider.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)

        spider.browser.page_source
        

        res = HtmlResponse(url = spider.browser.current_url, body = spider.browser.page_source, encoding = 'utf8', request = request)
        #print("==========================res")
        #print(spider.browser.page_source)
        #print("==========================res")
        return res

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest

        print("$$$$$$$$$$$$$$$$$$$$")
        print(len(response.xpath('//div/div/a/div/div/div/@style')))
        print(len(response.css('.shop-search-result-view__item')))

        if len(response.xpath('//div/div/a/div/div/div/@style')) != len(response.css('.shop-search-result-view__item')):
            spider.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            spider.browser.execute_script("window.scrollTo(100, 500);")
            spider.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(10)
            print("$$$$$$$$$$$$$$$$$$$$")
            print(len(response.xpath('//div/div/a/div/div/div/@style')))
            print(len(response.css('.shop-search-result-view__item')))

            # reason = response_status_message(response.status)
            if self._retry(request, response, spider) == True:
                print("asdfasdf")

        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)