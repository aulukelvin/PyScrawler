# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class NewsItem(Item):
    title = Field()
    url = Field()
    
class NewsStory(Item):
    title = Field()
    body = Field()
    excerpt = Field()
    url = Field()
