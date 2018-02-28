
# -*- coding: utf-8 -*-
import scrapy
import socket
from ..items import DmozItem

class ToScrapeSpiderXPath(scrapy.Spider):
    name = 'dmoz'
    allowed_domains = ["news.baidu.com"]
    start_urls = [

        "http://news.baidu.com"
    ]

    def parse(self, response):
        for sel in response.xpath('//ul/li'):
            socket.setdefaulttimeout(4)
            item = DmozItem()
            item['title'] = sel.xpath('a/text()').extract()
            item['link'] = sel.xpath('a/@href').extract()
            item['desc'] = sel.xpath('text()').extract()
            yield item

