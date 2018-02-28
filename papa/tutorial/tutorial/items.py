# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class DmozItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()

class DoubanItem(scrapy.Item):
    #排名位置
    title =scrapy.Field()
    #电影名称
    movie_name=scrapy.Field()
    #评分
    score=scrapy.Field()
    #评分人数
    score_num=scrapy.Field()
