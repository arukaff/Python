from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.loader import ItemLoader
from items import UnsplashItem
from itemloaders.processors import MapCompose
from urllib.parse import urljoin


class UnsplashImgsSpider(CrawlSpider):
    name = "unsplash_imgs"
    allowed_domains = ["unsplash.com"]
    start_urls = ["https://unsplash.com/images"]

    rules = (Rule(LinkExtractor(restrict_xpaths=("//body/div[@id='app']/div[1]/div[1]/div[5]/div[1]/div[2]/div[2]/ul/li/a")), callback='parse_item', follow=True),)
    
    def parse_item(self, response):
        loader = ItemLoader(item=UnsplashItem(), response=response)
        loader.default_input_processor = MapCompose(str.strip)

        loader.add_xpath('collection', '//header/h1/text()')

        image_urls = response.xpath("//figure[@data-testid='photo-grid-masonry-figure']/div/div/a/@href").getall()
        image_title = response.xpath("//figure[@data-testid='photo-grid-masonry-figure']/div/div/a/@title").getall()
        row_data=zip(image_title,image_urls)
        for row in row_data:
                url = self.start_urls+ row[1]
                loader.add_value('title', row[0])
                loader.add_value('image_url', url)

        yield loader.load_item()