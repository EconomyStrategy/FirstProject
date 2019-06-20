# -*- coding: utf-8 -*-
#import codecs, json
import MySQLdb 
from openpyxl import Workbook

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class FirstprojectPipeline(object):
    def __init__(self):
        # save data in database
        db = MySQLdb.Connect(host='localhost', user='root', passwd='123456', db='scrapydb', charset='utf8',use_unicode=True)
        # 游标/指针
        cursor = db.cursor()
        self.db = db
        self.cursor = cursor
        
        '''
        # excel file, write table header
        self.wb = Workbook()
        self.ws = self.wb.active
        self.ws.append(['text', 'author', 'tags'])
        '''
        
        '''
        # json file
        self.file = codecs.open('quotes.json', 'w', encoding='utf-8')
        '''
        
    def process_item(self, item, spider):
        
        try:
            sql="insert into quotes(text, author, tags) VALUES (%s, %s, %s)"
            self.cursor.execute(sql, (item['text'], item['author'], ','.join(item['tags'])))
            self.db.commit()
        except:
            print u'数据重复忽略不计'
            
        '''
        # excel file, write table header
        line = [item['text'], item['author'], ','.join(item['tags'])]
        #line = line.encode('unicode-escape').decode('string_escape')
        self.ws.append(line)
        self.wb.save('quotes.xlsx')
        '''
        '''
        # json file
        lines = json.dumps(dict(item), ensure_ascii = False) + '\n'
        self.file.write(lines)
        '''
        
        return item
    
    def spider_closed(self, spider):
        pass
        # json file
        #self.file.close()
        
        

