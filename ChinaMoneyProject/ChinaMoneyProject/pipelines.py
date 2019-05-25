# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql

class ChinamoneyprojectPipeline(object):
    def process_item(self, item, spider):
        return item

class MysqlPipeline(object):
    def open_spider(self, spider):
        # 链接数据库
		# 需在数据库中创建表，并填写数据库地址及密码
        self.conn = pymysql.Connect(host='*****', port=3306, user='***', password='*****', db='sqh_test', charset='utf8')
        # 获取游标
        self.cursor = self.conn.cursor()

        self.f = open('IO1.txt', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        # 拼接sql语句

        sql = 'insert into chinamoney (title,draftPath,releaseDate,contentId) values("%s","%s","%s","%s")' % (item['title'], item['draftPath'], item['releaseDate'], item['contentId'])

        try:
            self.cursor.execute(sql)

            # 提交
            self.conn.commit()
        except Exception as e:
            self.f.write(str(e))
            self.conn.rollback()

        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()