# -*- coding: utf-8 -*-
import scrapy


class SpiderItem(scrapy.Item):
    url = scrapy.Field()
    page = scrapy.Field()
    date_last_seen = scrapy.Field()
    title = scrapy.Field()
    h1 = scrapy.Field()
    h2 = scrapy.Field()
    h3 = scrapy.Field()
    h4 = scrapy.Field()
    h5 = scrapy.Field()
    h6 = scrapy.Field()
    p = scrapy.Field()
    ol = scrapy.Field()
    ul = scrapy.Field()
    span = scrapy.Field()

