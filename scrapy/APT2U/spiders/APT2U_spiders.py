# -*- coding: utf-8 -*-
import scrapy
#import sys
from scrapy.spiders import Spider
from scrapy.selector import HtmlXPathSelector
from APT2U.items import APT2UItem
from scrapy.http import Request
from scrapy.selector import Selector
#reload(sys)
#sys.setdefaultencoding('utf-8')
 
class APT2U_Spider(scrapy.Spider):
    name = "APT2U"  #spider �̸�
    allowed_domains = ["www.apt2you.com"]
    start_urls = ["http://www.apt2you.com/houseSaleSimpleInfo.do"]
     
    def parse(self, response):
        hxs = Selector(response)
        selects =[]
        selects = hxs.xpath('//tbody[@class="line"]/tr')
        items = []
        for sel in selects:
            item = APT2UItem()
            item['aptname'] = sel.xpath('th[@scope="row"]/a[@href="#none"]/text()').extract()
            item['link'] = sel.xpath('th[@scope="row"]/a/@onclick').re('\d+')
            item['link'][0] = "http://www.apt2you.com/houseSaleDetailInfo.do?manageNo="+item['link'][0]
            item['company'] = sel.xpath('td[1]/text()').extract()
            item['receiptdate'] = sel.xpath('normalize-space(td[2]/text())').extract()
            item['result_date'] = sel.xpath('td[@class="end"]/text()').extract()
            items.append(item)
        return items