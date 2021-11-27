import scrapy


class AccupassSpider(scrapy.Spider):
    name = 'accupass'
    allowed_domains = ['accupass.com']
    start_urls = ['http://accupass.com/']

    def parse(self, response):
        pass
