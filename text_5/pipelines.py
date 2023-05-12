# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import pymongo
class Text5Pipeline:
    def open_spider(self,spider):
        self.client = pymongo.MongoClient(host='127.0.0.1',port=27017)
        self.db =self.client['rehat']
        self.com = self.db['com']

    def process_item(self, item, spider):
        #第一个参数  判断  第二个参数 插入的数据  第三个
        self.com.update_one({'detail_url':item['detail_url']},{'$set':dict(item)},True)
        return item

    def close_spider(self,spider):
        self.client.close()
