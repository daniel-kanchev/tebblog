import scrapy
from scrapy.loader import ItemLoader
from tebblog.items import Article
from itemloaders.processors import TakeFirst


class TebSpider(scrapy.Spider):
    name = 'teb'
    allowed_domains = ['blogteb.com']
    # oldest article, scrape from here for all articles
    # start_urls = ['https://www.blogteb.com/yolo-dunyasi-icin-geri-sayim-basladi/']

    # newest article at time of posting, scrape from here for new articles
    start_urls = ['https://www.blogteb.com/oturdugunuz-yerden-dunyaca-unlu-muze-ve-sergileri-gezin/']

    def parse(self, response):
        yield response.follow(response.url, self.parse_article, dont_filter=True)
        next_page = response.xpath('//div[@class="mkdf-blog-single-next"]/a/@href').get()
        if next_page:
            yield response.follow(next_page, self.parse)

    def parse_article(self, response):
        item = ItemLoader(Article())
        item.default_output_processor = TakeFirst()

        title = response.xpath('//h1[@class="mkdf-title-text"]//text()').get()
        date = response.xpath('//div[@class="mkdf-title-post-info"]//a//text()').get().strip()
        content = response.xpath('//div[@class="mkdf-post-text"]//text()').getall()
        content = '\n'.join(content).strip()
        tags = response.xpath('//div[@class="mkdf-tags"]//text()').getall()
        tags = [tag for tag in tags if tag.strip()]
        tags = ','.join(tags)

        item.add_value('title', title)
        item.add_value('date', date)
        item.add_value('tags', tags)
        item.add_value('link', response.url)
        item.add_value('content', content)

        return item.load_item()
