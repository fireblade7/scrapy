# -*- coding: utf-8 -*-
import scrapy
from scrapy.item import Item, Field
 
class APT2UItem(scrapy.Item):
    aptname = scrapy.Field()        #주택명
    link = scrapy.Field()           #링크주소
    company = scrapy.Field()        #건설업체
    receiptdate = scrapy.Field()    #청약기간
    result_date = scrapy.Field()    #당첨자발표일