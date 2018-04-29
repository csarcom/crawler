import scrapy


class GizmodoItem(scrapy.Item):
    title = scrapy.Field()
    author = scrapy.Field()
    intro = scrapy.Field()
    post_url = scrapy.Field()
    author_url = scrapy.Field()
    category = scrapy.Field()
    date = scrapy.Field()
