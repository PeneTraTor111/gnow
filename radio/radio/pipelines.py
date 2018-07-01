# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3
import re
class RadioPipeline(object):
    def process_item(self, item, spider):
        return item

class RadioSqlitePipeline(object):

    PATH_TO_DB = "price.db"

    def __init__(self):
        self.connection = sqlite3.connect(self.PATH_TO_DB)
        self.cursor = self.connection.cursor()
        self.cursor.execute('''
        create table if not exists radio
        (
            ID integer primary key autoincrement,
            HEAD text,
            TIME text,
            HREF text,
            IMGSRC text,
            IMGTITLE text,
            DESCRIBE text
        );
    ''')

    def process_item(self,item,spider):
        head = item['head']
        time = item['time']
        href = item['href']
        imgSrc = item['imgSrc']
        imgTitle = item['imgTitle']
        describe = item['describe'] 
        
        self.cursor.execute('''
            insert into radio (HEAD,TIME,HREF,IMGSRC,IMGTITLE,DESCRIBE) values 
            (?,?,?,?,?,?)''',(head,time,href,imgSrc,imgTitle,describe))
        self.connection.commit()
        return item
