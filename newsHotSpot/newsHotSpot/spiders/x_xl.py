# -*- coding: utf-8 -*-
import scrapy


class xlCSSSpider(scrapy.Spider):
    name = "x_xl"
    start_urls = [
        'http://jhsjk.people.cn/result?keywords=习近平&year=206&button=搜索',
    ]

    def parse(self, response):
        # print(123)
        # print(response.css("div.fr>ul"))
        for quote in response.css("div.fr>ul>li"):
            # print('xxxxxxxxxxx', str(quote.xpath('./text()').extract_first())[str(quote.xpath('./text()').extract_first()).index('[')+1:str(quote.xpath('./text()').extract_first()).index(']')])
            yield {
                'input_date': str(quote.xpath('./text()').extract_first())[str(quote.xpath('./text()').extract_first()).index('[')+1:str(quote.xpath('./text()').extract_first()).index(']')],
                'title': quote.css("a::text").extract_first(),
                'url': response.urljoin(quote.css("a::attr(href)").extract_first()),
            }

        for nextPage in response.css("div.pagination>ul>li"):
            if nextPage.css('a::attr(rel)').extract_first() == 'next':
                next_page_url = nextPage.css('a::attr(href)').extract_first()
                if next_page_url is not None:
                    yield scrapy.Request(response.urljoin(next_page_url))
