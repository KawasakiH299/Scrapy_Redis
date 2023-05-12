import redis
import requests
from lxml import etree
from text_5.settings import REDIS_HOST,REDIS_PORT
r = redis.Redis(host=REDIS_HOST,port=REDIS_PORT)
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.62'}
response = requests.get(url='https://home.meishichina.com/recipe-type.html',headers=headers).text
html = etree.HTML(response)
type_response = html.xpath('//div[@class="category_sub clear"]/ul/li')
for types in type_response:
    name = types.xpath('./a/@title')[0]
    href = types.xpath('./a/@href')[0]
    # print(href)
    r.lpush('redhat:urls',href)