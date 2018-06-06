# -*- coding: utf-8 -*-
import scrapy


class xlCSSSpider(scrapy.Spider):
    name = "trump_tax"
    start_urls = [
        'https://www.wsj.com/search/term.html?KEYWORDS=donald%20trump%20tax&min-date=2017/11/25&max-date=2018/06/06&isAdvanced=true&daysback=90d&andor=AND&sort=relevance&source=wsjarticle,wsjblogs,wsjvideo,interactivemedia,sitesearch',
    ]

    def parse(self, response):
        # print(123)
        print(len(response.css("div.search-results-sector>div>div>ul.items>li")))
        for quote in response.css("div.search-results-sector>div>div>ul.items>li"):
            # print('xxxxxxxxxxx', str(quote.xpath('./text()').extract_first())[str(quote.xpath('./text()').extract_first()).index('[')+1:str(quote.xpath('./text()').extract_first()).index(']')])
            yield {
                'category': quote.css("div>div.headline-container>div.category>ul>li>a::text").extract_first(),
                'headline': quote.css("div>div.headline-container>h3.headline>a::text").extract_first(),
                'url': response.urljoin(
                    quote.css("div>div.headline-container>h3.headline>a::attr(href)").extract_first()),
                'article_info': quote.css(
                    "div>div.headline-container>div.article-info>ul>li>time::text").extract_first(),
                'summary': quote.css("div>div.headline-container>div.summary-container>p::text").extract_first(),
            }

            next_page_url = response.css("li.next-page>a::attr(href)")
            next_page_url = response.urljoin(next_page_url)
            if next_page_url is not None:
                yield scrapy.Request(response.urljoin(next_page_url))
