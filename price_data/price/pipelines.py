# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3
import re

class PricePipeline(object):
    def process_item(self, item, spider):
        return item

class PriceSqlitePipeline(object):

    PATH_TO_DB = "../price.db"

    def __init__(self):
        self.connection = sqlite3.connect(self.PATH_TO_DB)
        self.cursor = self.connection.cursor()
        self.cursor.execute('''
        create table if not exists gameprice
        (
            ID integer primary key autoincrement,
            NAME text not null,
            AUS text,
            AUT text,
            BEL text,
            BGR text,
            CAN text,
            HRV text,
            CYP text,
            CZE text,
            DNK text,
            EST text,
            FIN text,
            FRA text,
            DEU text,
            GRC text,
            HUN text,
            IRL text,
            ITA text,
            JPN text,
            LVA text,
            LTU text,
            LUX text,
            MLT text,
            MEX text,
            NLD text,
            NZL text,
            NOR text,
            POL text,
            PRT text,
            ROU text,
            RUS text,
            SVK text,
            SVN text,
            ZAF text,
            ESP text,
            SWE text,
            CHE text,
            GBR text,
            USA text
        );
    ''')

    def process_item(self,item,spider):
        name = item['name']
        price = []
        for p in item['price']:
            p_value = re.search('[0-9]+.[0-9]+',p) 
            if (p_value):
                price.append(p_value.group())
            else:
                price.append('N/A')
        
        self.cursor.execute('''
            insert into gameprice (NAME,AUS,AUT,BEL,BGR,CAN,HRV,CYP,CZE,DNK,EST,FIN,FRA,DEU,GRC,HUN,IRL,ITA,JPN,
            LVA,LTU,LUX,MLT,MEX,NLD,NZL,NOR,POL,PRT,ROU,RUS,SVK,SVN,ZAF,ESP,SWE,CHE,GBR,USA) values 
            (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',(str(name),price[0],price[1],price[2],price[3],price[4], \
            price[5],price[6],price[7],price[8],price[9],price[10],price[11],price[12],price[13],price[14], \
            price[15],price[16],price[17],price[18],price[19],price[20],price[21],price[22],price[23],price[24], \
            price[25],price[26],price[27],price[28],price[29],price[30],price[31],price[32],price[33],price[34], \
            price[35],price[36],price[37]))
        self.connection.commit()
        return item
