from scrapy.spiders import Spider
from scrapy.selector import Selector

from event_scraper.items import EventScraperItem


class EventbriteSpider(Spider):
    name = "eventbrite"
    allowed_domains = ["vimbly.com"]
    start_urls = [
        "https://www.vimbly.com/"
    ]

    def parse(self, response):
        sel = Selector(response)
        sites = sel.xpath('//*')
        items = []

        for site in sites:
            item = EventScraperItem()
            item['name'] = map(unicode.strip, site.xpath('//h2/a/text()').extract())
            item['date'] = map(unicode.strip, site.xpath('//a[@class="firstTime"]/text()').extract())
            item['price'] = map(unicode.strip, site.xpath('//span[@class="currentPrice"]/text()').extract())
            item['venue'] = map(unicode.strip, site.xpath('//div[@class="description"]/text()').extract())
            items.append(item)

        return items
