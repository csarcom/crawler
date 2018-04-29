import scrapy
class TestSpider(scrapy.Spider):
    name = "test"

    start_urls = [
        "http://gizmodo.uol.com.br/",
    ]

    def parse(self, response):
        with open('/home/charles/projects/cheesecake/spiders/gizmodo.html', 'wb') as f:
            f.write(response.body)