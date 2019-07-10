# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.shell import inspect_response


class EmuparadiseSpider(CrawlSpider):
    name = 'emuparadise'
    allowed_domains = ['www.emuparadise.me']
    start_urls = [
        'https://www.emuparadise.me/Sega_Genesis_-_Sega_Megadrive_ROMs/6',
        'https://www.emuparadise.me/Nintendo_64_ROMs/9',
        'https://www.emuparadise.me/Super_Nintendo_Entertainment_System_(SNES)_ROMs/5',
        'https://www.emuparadise.me/Sega_Master_System_ROMs/15'
    ]

    rules = (
        Rule(LinkExtractor(restrict_xpaths=['//a[@class="letter"]']), follow=True),
        Rule(LinkExtractor(restrict_xpaths=['//a[@class="index gamelist"]']), callback="parse_game", follow=True)
    )

    def parse_game(self, response):
        review = " ".join(response.xpath("//div[@id='content']//table//td[@bgcolor='#4C6977']/font[@size='2']//text()").extract())
        name = response.xpath("//h1/text()").extract_first().strip()
        yield {
            "name": name,
            "review": review
        }
        # inspect_response(response, self)
        # item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        # return item
