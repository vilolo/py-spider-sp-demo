# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import json
import pymysql

class SpideronePipeline1(object):

    def __init__(self):
        self.filename = open('thousandPic.json','w', encoding="utf-8")


    def process_item(self, item, spider):
        print("into SpideronePipeline 111111111111")
        #  ensure_ascii=False 可以解决 json 文件中 乱码的问题。
        text = json.dumps(dict(item), ensure_ascii=False) + ',\n'   #  这里是一个字典一个字典存储的，后面加个 ',\n' 以便分隔和换行。
        self.filename.write(text)

        return item

    def close_spider(self,spider):
        self.filename.close()

class SpideronePipeline2(object):

    def __init__(self):
        self.filename = open('thousandPic.json','w', encoding="utf-8")


    def process_item(self, item, spider):
        print("into SpideronePipeline 222222222222")
        #  ensure_ascii=False 可以解决 json 文件中 乱码的问题。
        text = json.dumps(dict(item), ensure_ascii=False) + ',\n'   #  这里是一个字典一个字典存储的，后面加个 ',\n' 以便分隔和换行。
        self.filename.write(text)

        return item

    def close_spider(self,spider):
        self.filename.close()

class BuckPipeline(object):
    def __init__(self):
        print("=============== into BuckPipeline =======================")
        pass

    def process_item(self, item, spider):
        conn = pymysql.connect(host='198.35.45.87', user='test', password='123!@#QWEasd', database='sp', charset='utf8')
        cursor = conn.cursor()

        try:
            with conn.cursor() as cursor:
                sql = 'insert into sp_store_detail_log (crawlid, name, store_id, products, joined, followers, following, rating) values(%s, %s, %s, %s, %s, %s, %s)'

                # 执行SQL语句
                cursor.execute(sql, (item['crawlid'], item['name'], item['storeId'], item['products'], item['joined'], item['followers'], item['following'], item['rating']))
            
                # 连接完数据库并不会自动提交，所以需要手动 commit 你的改动
                conn.commit()

            # with conn.cursor() as cursor:
            #     # 读取单条记录
            #     sql = "SELECT `id`, `name` FROM `sp_store_detail_log` WHERE id=%s"
            #     cursor.execute(sql, ('3',))
            #     result = cursor.fetchone()

            #     print(result)
        
        finally:
            # 关闭数据库连接
            conn.close()