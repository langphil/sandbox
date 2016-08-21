import scrapy

from tutorial.items import DmozItem

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    ]

    # Traversing to get to the information that I need
    # Using a CSS class to idenitfy the area to scrape, then tightening identification with xpath. Removed elements from the output with normalize-space()
    def parse(self, response):
        for sel in response.xpath('//div[@class="title-and-desc"]'):
            item = DmozItem()
            item['title'] = sel.xpath('a/div/text()').extract()
            item['link'] = sel.xpath('a/@href').extract()
            item['desc'] = sel.xpath('normalize-space(div/text())').extract()
            yield item
