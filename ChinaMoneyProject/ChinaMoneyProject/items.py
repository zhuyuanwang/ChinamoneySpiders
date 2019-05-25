# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class ChinamoneyprojectItem(scrapy.Item):

    #标题
    title = scrapy.Field()

    #下一级PDF链接
    draftPath = scrapy.Field()

    #时间
    releaseDate = scrapy.Field()

    #拼接PDF下载页面的code
    contentId = scrapy.Field()
