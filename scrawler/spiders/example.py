# -*- coding: utf-8 -*-
import scrapy


class ExampleSpider(scrapy.Spider):
    name = "example"
    allowed_domains = ["www.bbc.com"]
    start_urls = (
        'http://www.bbc.com/',
    )

    def parse(self, response):
        pass
