from scrapy.spiders import Spider
from scrapy.http import Request

from webscrapy.items import SpyderItem


class GizmodoSpider(Spider):
    name = 'gizmodo'
    pages = 2

    def start_requests(self):
        pages = [Request('http://gizmodo.uol.com.br/page/%s' % page, callback=self.parse) 
                 for page in range(1, self.pages + 1)]
        return pages

    def parse(self, response):
        for post in response.css('#loop-chamadas')[0].css('.chamada'):
            item = SpyderItem()
            item['title'] = post.css('.title-1000 a::attr(title)').extract_first()
            item['intro'] = post.css('.chamada-intro a::text').extract_first().strip()
            item['author'] = post.css('.por a::text').extract_first()
            item['post_url'] = post.css('.chamada-intro a::attr(href)').extract_first()
            item['author_url'] = post.css('.por a::attr(href)').extract_first()
            item['category'] = post.css('.chamada-cat a::text').extract_first()
            yield Request(item['post_url'], callback=self.parse_post, meta={'item': item})

    def parse_post(self, response):
        item = SpyderItem(response.meta['item'])
        item['date'] = response.css('.social-title::text').extract()[1].strip()
        yield item
