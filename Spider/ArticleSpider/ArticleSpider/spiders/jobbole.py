# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
import urllib


from ArticleSpider.items import ArticleItem
class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/all-posts/']

    def parse(self, response):
        post_urls = response.css("#archive .floated-thumb .post-thumb a::attr(href)").extract()
        for post_url in post_urls:
            yield Request(url=urllib.parse.urljoin(response.url, post_url), callback=self.parse_detail)

        next_url = response.css(".next.page-numbers::attr(href)").extract_first()
        if next_url:
            yield Request(url=urllib.parse.urljoin(response.url, next_url), callback=self.parse)

    def parse_detail(self, response):
        #pass
        # extract title
        title = response.css(".entry-header h1::text").extract_first()
        #print(title)

        # create_time
        create_time = response.css('.entry-meta-hide-on-mobile::text').extract_first().strip()[:10]
        #print(create_time)

        # content
        content = response.css('.entry').extract_first()
        #print(content)

        item = ArticleItem()
        item['title'] = title
        item['create_date'] = create_time
        item['content'] = content
        yield  item



