import subprocess

from celery import shared_task
from scrapy.cmdline import execute
from scrapy.crawler import CrawlerProcess, CrawlerRunner
from scrapy.utils.project import get_project_settings
from twisted.internet import reactor

from scrapy_app.gold_spider.gold_spider.spiders.gold import GoldSpider

scrapy_project_path = "/home/momentum/PycharmProjects/django_scrapy_mixing/scrapy_app/gold_spider"

@shared_task
def run_scrapy_spider():
    subprocess.run(['scrapy', 'crawl', 'gold'], cwd=scrapy_project_path)
















