from scrapy.crawler import CrawlerProcess
from scrapy.utils.reactor import install_reactor
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings

from spiders.unsplash_imgs import UnsplashImgsSpider

if __name__ =='__main__':
    install_reactor('twisted.internet.asyncioreactor.AsyncioSelectorReactor')
    configure_logging()
    settings = get_project_settings()
    process = CrawlerProcess(settings)
    process.crawl(UnsplashImgsSpider)
    process.start()