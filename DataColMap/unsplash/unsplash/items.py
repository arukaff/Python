# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class UnsplashItem(scrapy.Item):
    collection = scrapy.Field()
    title = scrapy.Field()
    image_url = scrapy.Field()
    images = scrapy.Field()
