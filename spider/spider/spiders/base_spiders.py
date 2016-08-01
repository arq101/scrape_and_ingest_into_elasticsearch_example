# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider

from spider.items import SpiderItem


class BaseSpider(CrawlSpider):
    name = ''
    allowed_domains = []
    start_urls = []
    custom_settings = {
        'BOT_NAME': 'recipe_scraper',
        'CONCURRENT_REQUESTS_PER_DOMAIN': 4,
        'DEPTH_LIMIT': 3,
        'DOWNLOAD_DELAY': 3,
        'REDIRECT_ENABLED': True,
    }
    rules = []

    def parse_item(self, response):
        item = SpiderItem()
        item['url'] = response.url
        # whole page is currently not required
        # item['page'] = response.xpath('//html').extract()
        item['date_last_seen'] = str(response.headers.get('Date'), 'utf-8')
        item['title'] = response.xpath('//title/text()').extract()
        item['h1'] = response.xpath('//h1/text()').extract()
        item['h2'] = response.xpath('//h2/text()').extract()
        item['h3'] = response.xpath('//h3/text()').extract()
        item['h4'] = response.xpath('//h4/text()').extract()
        item['h5'] = response.xpath('//h5/text()').extract()
        item['h6'] = response.xpath('//h6/text()').extract()
        item['p'] = response.xpath('//p/text()').extract()
        item['p'] += response.xpath('//p/b/text()').extract()
        item['ol'] = response.xpath('//ol/li/text()').extract()
        item['ul'] = response.xpath('//ul/li/text()').extract()
        item['span'] = response.xpath('//span/text()').extract()
        yield item


class BaseFashionSpider(BaseSpider):
    custom_settings = {
        'BOT_NAME': 'fashion_scraper',
        'CONCURRENT_REQUESTS_PER_DOMAIN': 4,
        'DEPTH_LIMIT': 3,
        'DOWNLOAD_DELAY': 3,
        'REDIRECT_ENABLED': True,
    }
