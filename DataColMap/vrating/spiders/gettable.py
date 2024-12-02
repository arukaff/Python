import scrapy


class GettableSpider(scrapy.Spider):
    name = "gettable"
    allowed_domains = ["technical.city"]
    start_urls = ["https://technical.city/ru/video/rating"]
   

    def parse(self, response):
        if response.status == 200 :
            try:
                data_header=response.xpath("//th/div/div[1]/text()")
                rows=response.xpath("//tr[contains(@id,'itemrow')]")
                for row in rows:
                    try:
                        cells=row.xpath(".//td//text()") 
                        ls=[]
                        try:
                            for s in cells:
                                    s=str(s).strip()
                                    if len(s)>0:
                                        ls.append(s)
                            tr={}
                            for i in range(len(data_header)):
                                    tr[str(data_header[i])]=ls[i]
                            yield tr
                        except Exception as e:
                            print(e)
                    except Exception as e:
                        print(e)
            except Exception as e:
                 print(e)




