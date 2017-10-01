# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
class BlogPipeline(object):

    def __init__(self):
        self.conn = pymysql.connect(host='localhost', user='root', password='lw54934', db='baidu')

    def process_item(self, item, spider):

            name = item['name'][0]
            url = item['url'][0]
            author = item['author'][0]
            skim = item['skim'][0]
            sort = item['sort'][0]

            sql = "insert into log(name,url,author,skim,sort)VALUES('"+name+"'" \
                  ", '"+url+"', '"+author+"','"+skim+"','"+sort+"')"
            self.conn.query(sql)
            self.conn.commit()
            return item

    def close_spider(self, spider):
        self.conn.close()
