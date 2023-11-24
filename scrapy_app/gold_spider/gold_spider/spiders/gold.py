import scrapy
import os
import django
import sys

django_project_path = "/home/momentum/PycharmProjects/django_scrapy_mixing"
sys.path.append(django_project_path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_scrapy_mixing.settings')
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
django.setup()
import re

from ..items import GoldSpiderItem
from scrapy_app.models import GoldPrice

class GoldSpider(scrapy.Spider):
    name = "gold"
    start_urls = ["https://www.tgju.org/profile/geram18/charts"]
    extracted_data = []

    def parse(self, response):
        items = GoldSpiderItem()
        price = response.css('.value > span:nth-child(1)').css('::text').extract()
        items['price'] = price
        self.extracted_data.append({
            'price': price
        })
        x = GoldPrice()
        x.price = price[0]
        x.save()

        yield items

