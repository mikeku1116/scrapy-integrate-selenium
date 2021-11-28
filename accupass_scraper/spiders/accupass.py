import scrapy
from scrapy_selenium import SeleniumRequest


class AccupassSpider(scrapy.Spider):
    name = 'accupass'
    allowed_domains = ['accupass.com']
    start_urls = ['http://accupass.com/']

    def start_requests(self):
        yield SeleniumRequest(url='https://www.accupass.com/?area=north', callback=self.parse)

    def parse(self, response):

        titles = response.css("p.style-f13be39c-event-name::text").getall()

        for title in titles:
            print(title)
