from scrapy.spiders import Spider
from scrapy.selector import Selector

from event_scraper.items import EventScraperItem


class EventbriteSpider(Spider):
    name = "eventbrite"
    allowed_domains = ["eventbrite.ca"]
    start_urls = [
        "https://www.eventbrite.ca/d/canada--toronto/events/"
    ]

    def parse(self, response):
        sel = Selector(response)
        sites = sel.xpath('//*')
        items = []

        for site in sites:
            item = EventScraperItem()
            item['name'] = map(unicode.strip, site.xpath('//div[@class="list-card__title"]/text()').extract())
            item['date'] = map(unicode.strip, site.xpath('//time[@class="list-card__date"]/text()').extract())
            item['price'] = map(unicode.strip, site.xpath('//span[@class="list-card__label"]/text()').extract())
            item['venue'] = map(unicode.strip, site.xpath('//div[@class="list-card__venue"]/text()').extract())
            items.append(item)

        return items
