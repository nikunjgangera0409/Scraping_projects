# -*- coding: utf-8 -*-
import scrapy


class ResultSpider(scrapy.Spider):
    name = 'result'
    allowed_domains = ['https://goldbet7.com/casinoresults/dt202']
    start_urls = ['http://https://goldbet7.com/casinoresults/dt202/']

    def parse(self, response):
        pass
