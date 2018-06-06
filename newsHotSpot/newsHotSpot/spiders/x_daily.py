import scrapy
import json
import datetime


# import sys
# sys.path.append('/test')
# from test import test

def getYesterday(days):
    today = datetime.date.today()
    oneday = datetime.timedelta(days=days)
    yesterday = today - oneday
    return yesterday.strftime('%Y%m%d')


class QuotesSpider(scrapy.Spider):
    name = "x_daily"
    start_urls = [
        'http://cpc.people.com.cn/data/xjp/20180606.json',
    ]

    def parse(self, response):
        sites = json.loads(response.body_as_unicode())
        for site in sites:
            yield {
                'input_date': site['input_date'],
                'summary': site['summary'],
                'image_title': site['image_title'],
                'title': site['title'],
                'origin_url': site['origin_url'],
                'url': site['url']
            }

        for i in range(0, 30):
            next_page = 'http://cpc.people.com.cn/data/xjp/' + getYesterday(i) + '.json'
            if next_page is not None:
                yield response.follow(next_page, callback=self.parse)
