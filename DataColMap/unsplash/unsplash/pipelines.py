from scrapy.pipelines.images import ImagesPipeline


class CustomImagesPipeline(ImagesPipeline):
    def file_path(self, request, response=None, info=None, *, item=None):
        print()
        return f"{item['collection']}/{item['title']}.jpg"
    
    def media_downloaded(self, response, request, info, *, item = None):
        return super().media_downloaded(response, request, info, item=item)
    
    def get_media_requests(self, item, info):
        print()
        return super().get_media_requests(item, info)
    def process_item(self, item, spider):
        print()
        return super().process_item(item, spider)

