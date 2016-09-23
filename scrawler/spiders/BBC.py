# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.selector import Selector
from scrawler.items import NewsItem

class ExampleSpider(Spider):
    name = "bbcSpider"
    Domain = "www.bbb.com"
    proxy = ""
    allowed_domains = ["www.bbc.com"]
    start_urls = (
        'http://www.bbc.com/news',
    )

    def parse(self, response):
        titles = Selector(response).xpath('//div[@id="comp-top-story-1"]/div/div')
        titles += Selector(response).xpath('//div[@class="pigeon-item__body"]')
        titles += Selector(response).xpath('//div[@class="pigeon-item faux-block-link"]')
        titles += Selector(response).xpath('//div[@class="macaw-item__body"]')
    #    titles += Selector(response).xpath('//div[@class="titanis__title titanis__title--fadein"]')
        titles += Selector(response).xpath('//div[@class="macaw-item__body"]')
        titles += Selector(response).xpath('//div[@class="sparrow-item__body"]')
        
        self.logger.info("totally grabbed %s titles.", len(titles))
        
        for title in titles:
            newsItem = NewsItem()
            newsItem['title'] = title.xpath('a/h3/span[@class="title-link__title-text"]/text()').extract()
            newsItem['url'] = title.xpath('a[@class="title-link"]/@href').extract()
            
            self.logger.info("title: %s\t %s", newsItem['title'], newsItem['url']) 
            yield newsItem               
            
            