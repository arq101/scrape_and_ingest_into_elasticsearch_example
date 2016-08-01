# -*- coding: utf-8 -*-
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

from .base_spiders import BaseFashionSpider


class BucketsAndSpadesBlog(BaseFashionSpider):
    name = 'fashion_bucketsandspadesblog'
    start_urls = ['http://www.bucketsandspadesblog.com/']
    allowed_domains = ['bucketsandspadesblog.com']
    rules = [
        Rule(
            LinkExtractor(allow=['\d{4}/\d{2}/']),
            callback='parse_item',
            follow=True
        )
    ]


class FiveInchAndUp(BaseFashionSpider):
    name = 'fashion_5inchandup'
    start_urls = ['http://5inchandup.blogspot.co.uk']
    allowed_domains = ['5inchandup.blogspot.co.uk']
    rules = [
        Rule(
            LinkExtractor(allow=['\d{4}/\d{2}/']),
            callback='parse_item',
            follow=True
        )
    ]


class CocosTeaParty(BaseFashionSpider):
    name = 'fashion_cocosteaparty'
    start_urls = ['http://cocosteaparty.com/']
    allowed_domains = ['cocosteaparty.com']
    rules = [
        Rule(
            LinkExtractor(allow=['\d{4}/\d{2}/']),
            callback='parse_item',
            follow=True
        )
    ]


class EnBrogue(BaseFashionSpider):
    name = 'fashion_enbrogue'
    start_urls = ['http://enbrogue.com/']
    allowed_domains = ['enbrogue.com']
    rules = [
        Rule(
            LinkExtractor(allow=['\d{4}/\d{2}/\d{2}/']),
            callback='parse_item',
            follow=True
        )
    ]


class GaryPepperGirl(BaseFashionSpider):
    name = 'fashion_garypeppergirl'
    start_urls = ['http://garypeppergirl.com/']
    allowed_domains = ['garypeppergirl.com']
    rules = [
        Rule(
            LinkExtractor(allow=['\d{4}/\d{2}/']),
            callback='parse_item',
            follow=True
        )
    ]


class Indtl(BaseFashionSpider):
    name = 'fashion_indtl'
    start_urls = ['http://indtl.com/']
    allowed_domains = ['indtl.com']
    rules = [
        Rule(
            LinkExtractor(allow=['style/']),
            callback='parse_item',
            follow=True
        )
    ]


class RainDropSoFapphire(BaseFashionSpider):
    name = 'fashion_raindropsofsapphire'
    start_urls = ['http://raindropsofsapphire.com/']
    allowed_domains = ['raindropsofsapphire.com']
    rules = [
        Rule(
            LinkExtractor(allow=['\d{4}/\d{2}/\d{2}/']),
            callback='parse_item',
            follow=True
        )
    ]


class RetroChick(BaseFashionSpider):
    name = 'fashion_retrochick'
    start_urls = ['http://retrochick.co.uk/style/']
    allowed_domains = ['retrochick.co.uk']
    rules = [
        Rule(
            LinkExtractor(allow=['\w+']),
            callback='parse_item',
            follow=True
        )
    ]
    custom_settings = {
        'BOT_NAME': 'fashion_scraper',
        'CONCURRENT_REQUESTS_PER_DOMAIN': 4,
        'DEPTH_LIMIT': 2,
        'DOWNLOAD_DELAY': 2,
        'REDIRECT_ENABLED': True,
    }


class StyleBubble(BaseFashionSpider):
    name = 'fashion_stylebubble'
    start_urls = ['http://stylebubble.co.uk/']
    allowed_domains = ['stylebubble.co.uk']
    rules = [
        Rule(
            LinkExtractor(allow=['style_bubble/\d{4}/\d{2}/']),
            callback='parse_item',
            follow=True
        )
    ]


class VanessaJackman(BaseFashionSpider):
    name = 'fashion_vanessajackman'
    start_urls = ['http://vanessajackman.blogspot.co.uk/']
    allowed_domains = ['vanessajackman.blogspot.co.uk']
    rules = [
        Rule(
            LinkExtractor(allow=['\d{4}/\d{2}/']),
            callback='parse_item',
            follow=True
        )
    ]


class WeWoreWhat(BaseFashionSpider):
    name = 'fashion_weworewhat'
    start_urls = ['http://weworewhat.com/']
    allowed_domains = ['weworewhat.com']
    rules = [
        Rule(
            LinkExtractor(allow=['outfits/', 'lifestyle/', 'interior']),
            callback='parse_item',
            follow=True
        )
    ]


class WishWishWish(BaseFashionSpider):
    name = 'fashion_wishwishwish'
    start_urls = ['http://wishwishwish.net/']
    allowed_domains = ['wishwishwish.net']
    rules = [
        Rule(
            LinkExtractor(allow=['\d{4}/\d{2}/']),
            callback='parse_item',
            follow=True
        )
    ]


class CamilleOverTheRainbow(BaseFashionSpider):
    name = 'fashion_camilleovertherainbow'
    start_urls = ['http://www.camilleovertherainbow.com/']
    allowed_domains = ['camilleovertherainbow.com']
    rules = [
        Rule(
            LinkExtractor(allow=['\d{4}/\d{2}/']),
            callback='parse_item',
            follow=True
        )
    ]


class DisneyRollerGirl(BaseFashionSpider):
    name = 'fashion_disneyrollergirl'
    start_urls = ['http://www.disneyrollergirl.net/']
    allowed_domains = ['disneyrollergirl.net']
    rules = [
        Rule(
            LinkExtractor(allow=['\w+']),
            callback='parse_item',
            follow=True
        )
    ]
    custom_settings = {
        'BOT_NAME': 'fashion_scraper',
        'CONCURRENT_REQUESTS_PER_DOMAIN': 4,
        'DEPTH_LIMIT': 2,
        'DOWNLOAD_DELAY': 2,
        'REDIRECT_ENABLED': True,
    }


class EllaLaPetiteAnglaise(BaseFashionSpider):
    name = 'fashion_ellalapetiteanglaise'
    start_urls = ['http://www.ella-lapetiteanglaise.com/']
    allowed_domains = ['ella-lapetiteanglaise.com']
    rules = [
        Rule(
            LinkExtractor(allow=['\w+']),
            callback='parse_item',
            follow=True
        )
    ]


class GarconJon(BaseFashionSpider):
    name = 'fashion_garconjon'
    start_urls = ['http://www.garconjon.com']
    allowed_domains = ['garconjon.com']
    rules = [
        Rule(
            LinkExtractor(allow=['\d{4}/\d{2}/']),
            callback='parse_item',
            follow=True
        )
    ]


class GreyFoxBlog(BaseFashionSpider):
    name = 'fashion_greyfoxblog'
    start_urls = ['http://www.greyfoxblog.com/']
    allowed_domains = ['greyfoxblog.com']
    rules = [
        Rule(
            LinkExtractor(allow=['\d{4}/\d{2}/']),
            callback='parse_item',
            follow=True
        )
    ]


class HannahLouis(BaseFashionSpider):
    name = 'fashion_hannahlouisef'
    start_urls = ['http://www.hannahlouisef.com/']
    allowed_domains = ['hannahlouisef.com']
    rules = [
        Rule(
            LinkExtractor(allow=['\d{4}/\d{2}/']),
            callback='parse_item',
            follow=True
        )
    ]


class LiseGrendene(BaseFashionSpider):
    name = 'fashion_lisegrendene'
    start_urls = [
        'http://www.lisegrendene.com.br/looks/',
        'http://www.lisegrendene.com.br/likes/',
        'http://www.lisegrendene.com.br/beauty/'
    ]
    allowed_domains = ['lisegrendene.com.br']
    rules = [
        Rule(
            LinkExtractor(allow=['looks/\d{4}/\d{1,2}/\d{1,2}/',
                                 'likes/\d{4}/\d{1,2}/\d{1,2}/',
                                 'beauty/\d{4}/\d{1,2}/\d{1,2}/']),
            callback='parse_item',
            follow=True
        )
    ]


class ManRepeller(BaseFashionSpider):
    name = 'fashion_manrepeller'
    start_urls = ['http://www.manrepeller.com/fashion']
    allowed_domains = ['manrepeller.com']
    rules = [
        Rule(
            LinkExtractor(allow=['\d{4}/\d{2}/']),
            callback='parse_item',
            follow=True
        )
    ]


class Nadiaaboulhosn(BaseFashionSpider):
    name = 'fashion_nadiaaboulhosn'
    start_urls = ['http://www.nadiaaboulhosn.com/']
    allowed_domains = ['nadiaaboulhosn.com']
    rules = [
        Rule(
            LinkExtractor(allow=['\d{4}/\d{2}/']),
            callback='parse_item',
            follow=True
        )
    ]


class NatalieHartley(BaseFashionSpider):
    name = 'fashion_nataliehartley'
    start_urls = ['http://nataliehartleywears.com/style/']
    allowed_domains = ['nataliehartleywears.com']
    rules = [
        Rule(
            LinkExtractor(allow=['style/']),
            callback='parse_item',
            follow=True
        )
    ]


class PandoraSykes(BaseFashionSpider):
    name = 'fashion_pandorasykes'
    start_urls = ['http://www.pandorasykes.com/category/fashion/']
    allowed_domains = ['pandorasykes.com']
    rules = [
        Rule(
            LinkExtractor(allow=['\w+']),
            callback='parse_item',
            follow=True
        )
    ]


class ParkAndCube(BaseFashionSpider):
    name = 'fashion_parkandcube'
    start_urls = ['http://www.parkandcube.com/category/style/']
    allowed_domains = ['parkandcube.com']
    rules = [
        Rule(
            LinkExtractor(allow=['\w+']),
            callback='parse_item',
            follow=True
        )
    ]


class PermanentStyle(BaseFashionSpider):
    name = 'fashion_permanentstyle'
    start_urls = ['http://www.permanentstyle.com/']
    allowed_domains = ['permanentstyle.com']
    rules = [
        Rule(
            LinkExtractor(allow=['\d{4}/\d{2}/']),
            callback='parse_item',
            follow=True
        )
    ]


class StellasWardrobe(BaseFashionSpider):
    name = 'fashion_stellaswardrobe'
    start_urls = ['http://www.stellaswardrobe.com/']
    allowed_domains = ['stellaswardrobe.com']
    rules = [
        Rule(
            LinkExtractor(allow=['\d{4}/\d{2}/']),
            callback='parse_item',
            follow=True
        )
    ]


class StreetPeeper(BaseFashionSpider):
    name = 'fashion_streetpeeper'
    start_urls = ['http://www.streetpeeper.com/']
    allowed_domains = ['streetpeeper.com']
    rules = [
        Rule(
            LinkExtractor(allow=['\w+']),
            callback='parse_item',
            follow=True
        )
    ]


class ThatPommieGirl(BaseFashionSpider):
    name = 'fashion_thatpommiegirl'
    start_urls = ['http://www.thatpommiegirl.com/']
    allowed_domains = ['thatpommiegirl.com']
    rules = [
        Rule(
            LinkExtractor(allow=['\d{4}/\d{2}/']),
            callback='parse_item',
            follow=True
        )
    ]


class TheFrugality(BaseFashionSpider):
    name = 'fashion_thefrugality'
    start_urls = ['http://www.the-frugality.com/']
    allowed_domains = ['the-frugality.com']
    rules = [
        Rule(
            LinkExtractor(allow=['\d{4}/\d{2}/']),
            callback='parse_item',
            follow=True
        )
    ]


class TheBlondeSalad(BaseFashionSpider):
    name = 'fashion_theblondesalad'
    start_urls = ['http://www.theblondesalad.com/']
    allowed_domains = ['theblondesalad.com']
    rules = [
        Rule(
            LinkExtractor(allow=['\d{4}/\d{2}/']),
            callback='parse_item',
            follow=True
        )
    ]


class TheDailyStreet(BaseFashionSpider):
    name = 'fashion_thedailystreet'
    start_urls = ['http://www.thedailystreet.co.uk/']
    allowed_domains = ['thedailystreet.co.uk']
    rules = [
        Rule(
            LinkExtractor(allow=['\d{4}/\d{2}/']),
            callback='parse_item',
            follow=True
        )
    ]


class TheFashionPolice(BaseFashionSpider):
    name = 'fashion_thefashionpolice'
    start_urls = ['http://www.thefashionpolice.net/']
    allowed_domains = ['thefashionpolice.net']
    rules = [
        Rule(
            LinkExtractor(allow=['\d{4}/\d{2}/']),
            callback='parse_item',
            follow=True
        )
    ]


class TheGentlemanBlogger(BaseFashionSpider):
    name = 'fashion_thegentlemanblogger'
    start_urls = ['http://www.thegentlemanblogger.com/']
    allowed_domains = ['thegentlemanblogger.com']
    rules = [
        Rule(
            LinkExtractor(allow=['\d{4}/\d{2}/']),
            callback='parse_item',
            follow=True
        )
    ]


# Currently not running this crawler
class TheSartorialist(BaseFashionSpider):
    name = 'fashion_thesartorialist'
    start_urls = ['http://www.thesartorialist.com/']
    allowed_domains = ['thesartorialist.com']
    rules = [
        Rule(
            LinkExtractor(allow=['men/', 'women/', 'photos/', 'paris/']),
            callback='parse_item',
            follow=True
        )
    ]
    custom_settings = {
        'BOT_NAME': 'fashion_scraper',
        'CONCURRENT_REQUESTS_PER_DOMAIN': 4,
        'DEPTH_LIMIT': 2,
        'DOWNLOAD_DELAY': 2,
        'REDIRECT_ENABLED': True,
    }


class AllThePrettyBirds(BaseFashionSpider):
    name = 'fashion_alltheprettybirds'
    start_urls = ['http://www.alltheprettybirds.com/']
    allowed_domains = ['alltheprettybirds.com']
    rules = [
        Rule(
            LinkExtractor(allow=['\w+']),
            callback='parse_item',
            follow=True
        )
    ]
    custom_settings = {
        'BOT_NAME': 'fashion_scraper',
        'CONCURRENT_REQUESTS_PER_DOMAIN': 4,
        'DEPTH_LIMIT': 2,
        'DOWNLOAD_DELAY': 2,
        'REDIRECT_ENABLED': True,
    }


class Peonylim(BaseFashionSpider):
    name = 'fashion_peonylim'
    start_urls = ['http://peonylim.com/fashion/']
    allowed_domains = ['peonylim.com']
    rules = [
        Rule(
            LinkExtractor(allow=['\w+']),
            callback='parse_item',
            follow=True
        )
    ]

