import scrapy
from scrapy.http import HtmlResponse


class HhruSpider(scrapy.Spider):
    name = "hhru"
    allowed_domains = ["aftershock.news"]
    start_urls = ["https://aftershock.news/"]

    def parse(self, response:HtmlResponse):
        print(response.status,response.url)
