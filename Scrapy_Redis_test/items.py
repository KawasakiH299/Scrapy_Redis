# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Text5Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #菜名
    name = scrapy.Field()
    #原料
    yuanliao = scrapy.Field()
    #步骤
    step = scrapy.Field()
    #判断的url
    detail_url = scrapy.Field()
