import scrapy
from text_5.items import Text5Item
from scrapy_redis.spiders import RedisSpider

class RedhatSpider(scrapy.Spider):
    name = 'redhat'
    # allowed_domains = ['www.baidu.com']
    start_urls = ['https://home.meishichina.com/recipe-type.html']
    redis_key = 'redhat:urls'
    def parse(self, response):
        type_response = response.xpath('//div[@class="category_sub clear"]/ul/li')
        for types in type_response:
            name = types.xpath('./a/@title').extract_first()
            href = types.xpath('./a/@href').extract_first()
            # print(name ,href)
            yield scrapy.Request(url=href,callback=self.parse_type)

    def parse_type(self,response):
    # def parse(self,response):
        index_response = response.xpath('//div[@id="J_list"]/ul/li')
        for type1 in  index_response:
            type_href = type1.xpath('./div[@class="detail"]/h2/a/@href').extract_first()
            type_name = type1.xpath('./div[@class="detail"]/h2/a/text()').extract_first()
            type_yuanliao = type1.xpath('./div[@class="detail"]/p[@class="subcontent"]/text()').extract_first()
            # print(type_yuanliao,type_href)
            yield scrapy.Request(url=type_href,callback=self.parse_step,meta={'type_name':type_name,'type_yuanliao':type_yuanliao,'detail_url':type_href})
        next_page = response.xpath('//div[@class="ui-page mt10"]/div/a[last()]/text()').extract_first()
        if next_page == '下一页':
            next_url = response.xpath('//div[@class="ui-page mt10"]/div/a[last()]/@href').extract_first()
            yield scrapy.Request(url=next_url,callback=self.parse_type)


    def parse_step(self,response):
        item = Text5Item()
        type_name = response.meta['type_name']
        type_yuanliao = response.meta['type_yuanliao']
        tyeps1 = response.xpath('//div[@class="recipeStep"]/ul/li/div[@class="recipeStep_word"]/text()').extract()
        # print(type_yuanliao,type_name,tyeps1)
        item['name']  =type_name
        item['yuanliao'] = type_yuanliao
        item['step']  = tyeps1
        detail_url =response.meta['detail_url']
        item['detail_url'] = detail_url
        return item
