# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
import codecs
 
class Apt2UPipeline(object):
    def __init__(self):
        self.file = codecs.open('Apt2U.json', 'w', encoding='utf-8') #크롤링 데이터를 저장할 파일 OPEN
         
    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n" #Item을 한줄씩 구성
        self.file.write(line) #파일에 기록
        return item
         
    def spider_closed(self, spider):
        self.file.close()   #파일 CLOSE
