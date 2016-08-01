# -*- coding: utf-8 -*-
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

from .base_spiders import BaseFashionSpider


class AsdaGoodLiving(BaseFashionSpider):
    name = 'fashion_asdagoodliving'
    start_urls = [
        'https://www.asdagoodliving.co.uk/style/fashion-tips/',
        'https://www.asdagoodliving.co.uk/home-ideas/',
    ]
    allowed_domains = ['asdagoodliving.co.uk', 'lifeandstyle.asda.com']
    rules = [
        Rule(
            LinkExtractor(allow=[
                'style/fashion-tips/', 'home-ideas/']),
            callback='parse_item',
            follow=True
        )
    ]


class AsdaLifeAndStyle(BaseFashionSpider):
    name = 'fashion_asdalifeandstyle'
    start_urls = ['http://lifeandstyle.asda.com/']
    allowed_domains = ['lifeandstyle.asda.com']
    rules = [
        Rule(
            LinkExtractor(allow=[
                'fashion/', 'home-garden/', 'women/', 'kids/', 'trends/']),
            callback='parse_item',
            follow=True
        )
    ]


class DorothyPerkins(BaseFashionSpider):
    name = 'fashion_dorothyperkins'
    start_urls = ['http://www.dorothyperkins.com/blog/']
    allowed_domains = ['dorothyperkins.com']
    rules = [
        Rule(
            LinkExtractor(
                allow=['blog/'],
                deny_domains=['pinterest.com', 'instagram.com']),
            callback='parse_item',
            follow=True
        )
    ]
    custom_settings = {
        'BOT_NAME': 'recipe_scraper',
        'CONCURRENT_REQUESTS_PER_DOMAIN': 4,
        'DEPTH_LIMIT': 2,
        'DOWNLOAD_DELAY': 3,
        'REDIRECT_ENABLED': True,
    }


class TuStyleSainsbury(BaseFashionSpider):
    name = 'fashion_tustylesainsbury'
    start_urls = ['https://tustyle.sainsburys.co.uk/']
    allowed_domains = ['tustyle.sainsburys.co.uk']
    custom_settings = {
        'BOT_NAME': 'recipe_scraper',
        'CONCURRENT_REQUESTS_PER_DOMAIN': 4,
        'DEPTH_LIMIT': 2,
        'DOWNLOAD_DELAY': 3,
        'REDIRECT_ENABLED': True,
    }
    rules = [
        Rule(
            LinkExtractor(allow=['\w+/']),
            callback='parse_item',
            follow=True
        )
    ]


class VeryBlog(BaseFashionSpider):
    name = 'fashion_very'
    start_urls = [
        'http://blog.very.co.uk/category/fashion/',
        'http://blog.very.co.uk/category/beauty/'
    ]
    allowed_domains = ['blog.very.co.uk']
    rules = [
        Rule(
            LinkExtractor(allow=['\d{4}/\d{2}/']),
            callback='parse_item',
            follow=True
        )
    ]


class Prima(BaseFashionSpider):
    name = 'fashion_prima'
    start_urls = ['http://www.prima.co.uk/fashion-and-beauty/']
    allowed_domains = ['prima.co.uk']
    rules = [
        Rule(
            LinkExtractor(allow=['fashion-and-beauty/']),
            callback='parse_item',
            follow=True
        )
    ]


class MarieClaire(BaseFashionSpider):
    name = 'fashion_marieclaire'
    start_urls = [
        'http://www.marieclaire.co.uk/fashion/',
        'http://www.marieclaire.co.uk/news/'
    ]
    allowed_domains = ['marieclaire.co.uk']
    rules = [
        Rule(
            LinkExtractor(allow=['fashion/', 'news/']),
            callback='parse_item',
            follow=True
        )
    ]


class ElleUk(BaseFashionSpider):
    name = 'fashion_elleuk'
    start_urls = [
        'http://www.elleuk.com/fashion/',
        'http://www.elleuk.com/beauty/',
        'http://www.elleuk.com/life-and-culture/'
    ]
    allowed_domains = ['elleuk.com']
    rules = [
        Rule(
            LinkExtractor(allow=[
                'fashion/', 'beauty/', 'life-and-culture/']),
            callback='parse_item',
            follow=True
        )
    ]


class Refinery29(BaseFashionSpider):
    name = 'fashion_refinery29'
    start_urls = [
        'http://www.refinery29.uk/beauty/',
        'http://www.refinery29.uk/fashion/'
    ]
    allowed_domains = ['refinery29.uk']
    rules = [
        Rule(
            LinkExtractor(allow=['\d{4}/\d{2}/']),
            callback='parse_item',
            follow=True
        )
    ]


class InStyle(BaseFashionSpider):
    name = 'fashion_instyle'
    start_urls = ['http://www.instyle.co.uk/fashion/']
    allowed_domains = ['instyle.co.uk']
    rules = [
        Rule(
            LinkExtractor(allow=['fashion/']),
            callback='parse_item',
            follow=True
        )
    ]


class Cosmopolitan(BaseFashionSpider):
    name = 'fashion_cosmopolitan'
    start_urls = [
        'http://www.cosmopolitan.co.uk/fashion/',
        'http://www.cosmopolitan.co.uk/beauty-hair/'
    ]
    allowed_domains = ['cosmopolitan.co.uk']
    rules = [
        Rule(
            LinkExtractor(allow=['fashion/', 'beauty-hair/']),
            callback='parse_item',
            follow=True
        )
    ]


class Stylist(BaseFashionSpider):
    name = 'fashion_stylist'
    start_urls = ['http://www.stylist.co.uk/fashion/']
    allowed_domains = ['stylist.co.uk']
    rules = [
        Rule(
            LinkExtractor(allow=['fashion/']),
            callback='parse_item',
            follow=True
        )
    ]


class Vogue(BaseFashionSpider):
    name = 'fashion_vogue'
    start_urls = [
        'http://www.vogue.co.uk/news/',
        'http://www.vogue.co.uk/fashion/trends/',
        'http://www.vogue.co.uk/beauty/'
    ]
    allowed_domains = ['vogue.co.uk']
    rules = [
        Rule(
            LinkExtractor(allow=[
                'news/\d{4}/\d{2}/\d{2}/',
                'fashion/trends/',
                'beauty/\d{4}/\d{2}/\d{2}/'
            ]),
            callback='parse_item',
            follow=True
        )
    ]


class Telegraph(BaseFashionSpider):
    name = 'fashion_telegraph'
    start_urls = ['http://www.telegraph.co.uk/fashion/']
    allowed_domains = ['telegraph.co.uk']
    rules = [
        Rule(
            LinkExtractor(allow=['fashion/']),
            callback='parse_item',
            follow=True
        )
    ]


class Independent(BaseFashionSpider):
    name = 'fashion_independent'
    start_urls = ['http://www.independent.co.uk/life-style/fashion/']
    allowed_domains = ['independent.co.uk']
    rules = [
        Rule(
            LinkExtractor(allow=['life-style/fashion/']),
            callback='parse_item',
            follow=True
        )
    ]


class BoeMagazine(BaseFashionSpider):
    name = 'fashion_boemagazine'
    start_urls = [
        'http://www.boemagazine.com/category/fashion/',
        'http://www.boemagazine.com/category/beauty/',
        'http://www.boemagazine.com/category/health/'
    ]
    allowed_domains = ['boemagazine.com']
    rules = [
        Rule(
            LinkExtractor(allow=['\d{4}/\d{2}/']),
            callback='parse_item',
            follow=True
        )
    ]


class Look(BaseFashionSpider):
    name = 'fashion_look'
    start_urls = [
        'http://www.look.co.uk/fashion/',
        'http://www.look.co.uk/hair-beauty/'
    ]
    allowed_domains = ['look.co.uk']
    rules = [
        Rule(
            LinkExtractor(allow=['fashion/', 'beauty/']),
            callback='parse_item',
            follow=True
        )
    ]


class GQMagazine(BaseFashionSpider):
    name = 'fashion_gq-magazine'
    start_urls = ['http://www.gq-magazine.co.uk/topic/fashion/']
    allowed_domains = ['gq-magazine.co.uk']
    rules = [
        Rule(
            LinkExtractor(allow=['article/', 'gallery/']),
            callback='parse_item',
            follow=True
        )
    ]


class GlamourMagazine(BaseFashionSpider):
    name = 'fashion_glamourmagazine'
    start_urls = [
        'http://www.glamourmagazine.co.uk/fashion/',
        'http://www.glamourmagazine.co.uk/news/'
    ]
    allowed_domains = ['glamourmagazine.co.uk']
    rules = [
        Rule(
            LinkExtractor(allow=['fashion/', 'news/fashion/\d{4}/\d{2}/d{2}/']),
            callback='parse_item',
            follow=True
        )
    ]


class MyFashionLife(BaseFashionSpider):
    name = 'fashion_myfashionlife'
    start_urls = [
        'http://www.myfashionlife.com/category/fashion-fix/',
        'http://www.myfashionlife.com/category/beauty/'
    ]
    allowed_domains = ['myfashionlife.com']
    rules = [
        Rule(
            LinkExtractor(allow=['archives/\d{4}/\d{2}/\d{2}/', 'gallery/']),
            callback='parse_item',
            follow=True
        )
    ]


class GoodHouseKeeping(BaseFashionSpider):
    name = 'fashion_goodhousekeeping'
    start_urls = ['http://www.goodhousekeeping.co.uk/fashion-beauty/']
    allowed_domains = ['goodhousekeeping.co.uk']
    rules = [
        Rule(
            LinkExtractor(allow=['fashion-beauty/']),
            callback='parse_item',
            follow=True
        )
    ]


class GoodToKnow(BaseFashionSpider):
    name = 'fashion_goodtoknow'
    start_urls = ['http://www.goodtoknow.co.uk/fashion/']
    allowed_domains = ['goodtoknow.co.uk']
    rules = [
        Rule(
            LinkExtractor(allow=['fashion/']),
            callback='parse_item',
            follow=True
        )
    ]


## This site was using anti scraping measures.
# class Mirror(BaseFashionSpider):
#     name = 'fashion_mirror'
#     start_urls = ['http://www.mirror.co.uk/3am/style/']
#     allowed_domains = ['mirror.co.uk']
#     rules = [
#         Rule(
#             LinkExtractor(allow=['3am/style/']),
#             callback='parse_item',
#             follow=True
#         )
#     ]


class DailyMail(BaseFashionSpider):
    name = 'fashion_dailymail'
    start_urls = ['http://www.dailymail.co.uk/femail/']
    allowed_domains = ['dailymail.co.uk']
    rules = [
        Rule(
            LinkExtractor(allow=['femail/']),
            callback='parse_item',
            follow=True
        )
    ]
