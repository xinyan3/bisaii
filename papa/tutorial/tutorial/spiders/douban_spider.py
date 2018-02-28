
# -*- coding: utf-8 -*-
from scrapy import Request
from scrapy import Spider
from ..items import DoubanItem

class DoubanMoveTop250(Spider):
    #定义spider命名
    name = 'douban_move_top250'
    #定义模拟浏览器登入的头文件
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    }
    #scrapy开始的网址
    def start_requests(self):
        url = 'https://movie.douban.com/top250'
        yield Request(url, headers=self.headers)

    def parse(self, response):
        item= DoubanItem()
        #定义response的开始节点
        movies = response.xpath('//ol[@class="grid_view"]/li')
        #抓取4个元素并输出到item里
        for movie in movies:
            item['title'] = movie.xpath(
                './/div[@class="pic"]/em/text()').extract()[0]
            item['movie_name'] = movie.xpath(
                './/div[@class="hd"]/a/span[1]/text()').extract()[0]
            item['score'] = movie.xpath(
                './/div[@class="star"]/span[@class="rating_num"]/text()'
            ).extract()[0]
            item['score_num'] = movie.xpath(
                './/div[@class="star"]/span[4]/text()'
            ).extract()[0]

            yield item
        #遍历下一页 ，返回网址给response
        next_url = response.xpath('//span[@class="next"]/a/@href').extract()
        #next_url= response.xpath('/*').extract()
        if next_url:
            next_url = 'https://movie.douban.com/top250' + next_url[0]
            yield Request(next_url, headers=self.headers)