# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql


class MysqlPipeline(object):
    def __init__(self):
        self.conn = None
        self.cur = None

    def open_spider(self, spider):
        self.conn = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            password='root',
            db='novel',
            charset='utf8',
        )
        self.cur = self.conn.cursor()

    def process_item(self, item, spider):
        if not hasattr(item, 'table_name'):
            return item
        cols, values = zip(*item.items())
        sql = "INSERT INTO `{}` ({}) VALUES ({}) ON DUPLICATE KEY UPDATE {}".format(
                  item.table_name,
                  ','.join(cols),
                  ','.join(['%s'] * len(values)),
                  ','.join(['`{}`=%s'.format(k) for k in cols])
              )
        self.cur.execute(sql, values*2)
        self.conn.commit()
        print(self.cur._last_executed)
        return item

    def close_spider(self, spider):
        self.cur.close()
        self.conn.close()
