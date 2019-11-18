# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import json

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
