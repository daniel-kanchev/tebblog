import scrapy


class Article(scrapy.Item):
    title = scrapy.Field()
    date = scrapy.Field()
    tags = scrapy.Field()
    link = scrapy.Field()
    content = scrapy.Field()
