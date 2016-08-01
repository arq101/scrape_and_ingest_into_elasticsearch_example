# -*- coding: utf-8 -*-
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

from .base_spiders import BaseSpider


class BBCGoodFood(BaseSpider):
    name = 'recipes_bbcgoodffood'
    start_urls = ['http://www.bbcgoodfood.com/recipes/']
    allowed_domains = ['bbcgoodfood.com']
    rules = [
        Rule(
            LinkExtractor(
                allow=['recipes/']
            ),
            callback='parse_item',
            follow=True
        )
    ]


class JamieOliver(BaseSpider):
    name = 'recipes_jamieoliver'
    start_urls = ['http://www.jamieoliver.com/recipes/']
    allowed_domains = ['jamieoliver.com']
    rules = [
        Rule(
            LinkExtractor(
                allow=['recipes/']
            ),
            callback='parse_item',
            follow=True
        )
    ]


class RealFoodTesco(BaseSpider):
    name = 'recipes_realfoodtesco'
    start_urls = ['https://realfood.tesco.com/recipes.html']
    allowed_domains = ['realfood.tesco.com']
    rules = [
        Rule(
            LinkExtractor(
                allow=['recipes/']
            ),
            callback='parse_item',
            follow=True
        )
    ]


class AllRecipes(BaseSpider):
    name = 'recipes_allrecipes'
    start_urls = ['http://allrecipes.co.uk/']
    allowed_domains = ['allrecipes.co.uk']
    rules = [
        Rule(
            LinkExtractor(
                allow=['recipes/']
            ),
            callback='parse_item',
            follow=True
        )
    ]


class LoveFoodHateWasteSpider(BaseSpider):
    name = 'recipes_lovefoodhatewaste'
    start_urls = ['http://www.lovefoodhatewaste.com/recipes/']
    allowed_domains = ['lovefoodhatewaste.com']
    rules = [
        Rule(
            LinkExtractor(
                allow=['recipes/']
            ),
            callback='parse_item',
            follow=True
        )
    ]


class BBCRecipes(BaseSpider):
    name = 'recipes_bbcrecipes'
    start_urls = ['http://www.bbc.co.uk/food/recipes/']
    allowed_domains = ['bbc.co.uk']
    rules = [
        Rule(
            LinkExtractor(
                allow=['food/collections/', 'food/recipes/']
            ),
            callback='parse_item',
            follow=True
        )
    ]


class AsdaGoodLiving(BaseSpider):
    name = 'recipes_asdagoodliving'
    start_urls = ['https://www.asdagoodliving.co.uk/food/recipes/']
    allowed_domains = ['asdagoodliving.co.uk']
    rules = [
        Rule(
            LinkExtractor(
                allow=['food/recipes/']
            ),
            callback='parse_item',
            follow=True
        )
    ]


class HomeMadeByYou(BaseSpider):
    name = 'recipes_homemadebyyou'
    start_urls = ['https://www.homemadebyyou.co.uk/recipes/']
    allowed_domains = ['homemadebyyou.co.uk']
    rules = [
        Rule(
            LinkExtractor(
                allow=['recipes/']
            ),
            callback='parse_item',
            follow=True
        )
    ]
