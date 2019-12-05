# -*- coding: utf-8 -*-
import scrapy

import spiderone.items

import pymysql

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

        conn = pymysql.connect(host='localhost', user='root', password='root', database='test', charset='utf8')

        # 得到一个可以执行SQL语句的光标对象
        cursor = conn.cursor()  # 执行完毕返回的结果集默认以元组显示
        # 得到一个可以执行SQL语句并且将结果作为字典返回的游标
        #cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        
        # 定义要执行的SQL语句
        sql = """
        CREATE TABLE USER1 (
        id INT auto_increment PRIMARY KEY ,
        name CHAR(10) NOT NULL UNIQUE,
        age TINYINT NOT NULL
        )ENGINE=innodb DEFAULT CHARSET=utf8;  #注意：charset='utf8' 不能写成utf-8
        """
        
        # 执行SQL语句
        cursor.execute(sql)
        
        # 关闭光标对象
        cursor.close()
        
        # 关闭数据库连接
        conn.close()

