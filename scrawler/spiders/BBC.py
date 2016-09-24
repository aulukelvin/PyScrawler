# -*- coding: utf-8 -*-
from scrapy import Spider, Request
from scrapy.selector import Selector
from scrawler.items import NewsItem, NewsStory

class ExampleSpider(Spider):
    name = "bbcSpider"
    BASE_URL = "http://www.bbc.com"
    Readability_Proxy = "https://www.readability.com/api/content/v1/parser?token=f066fd3ce1447d17d2fabb9c7075edbf0633466e&url="
    allowed_domains = ["www.bbc.com","www.readability.com"]
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
            
     #       self.logger.info("title: %s\t %s", newsItem['title'], newsItem['url']) 
            if newsItem['url']:
                yield Request(self.Readability_Proxy + self.BASE_URL + newsItem['url'][0], callback = self.parse_news_story)
                
    def parse_news_story(self, response):
        story = NewsStory()
        story['title'] = "asfdasdfasdfsadf"
        self.logger.info("safdddddddddddddddddddddddddddddddddddddddddddddddddddddddd")
        return story
        
            
            