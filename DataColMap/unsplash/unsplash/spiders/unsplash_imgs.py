import scrapy
from scrapy.loader import ItemLoader
from ..items import UnsplashItem    
from itemloaders.processors import MapCompose

class UnsplashImgsSpider(scrapy.Spider):
    name = "unsplash_imgs"
    allowed_domains = ["unsplash.com"]
    start_urls = ["https://unsplash.com/images"]

    def parse(self, response):
        categories = response.xpath("//li/a[contains(@href, 'photos')]")
        self.start_urls = ["https://unsplash.com"]
        for cat in categories:
            collection = cat.xpath(".//text()").get().strip()
            link = cat.xpath(".//@href").get()
            yield response.follow(url=link, callback=self.parse_collection, meta={'collection' : collection})

    def parse_collection(self, response):
        collection = response.request.meta['collection']
        imgs = response.xpath("//img[@data-testid='photo-grid-masonry-img']")
        loader = ItemLoader(item=UnsplashItem(), response=response)
        loader.default_input_processor = MapCompose(str.strip)

        for img in imgs:
            image_url = img.xpath(".//@src").get().strip()
            title = img.xpath(".//@alt").get().strip()
            loader.add_value('title', title)
            loader.add_value('image_url', image_url)
            loader.add_value('collection', collection)
        
        print(loader.item)
        yield loader.load_item()
        