#coding=utf8
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.selector import Selector
from tutorial.items import DoubanItem

class DoubanSpider(CrawlSpider):
    name = 'douban.com'
    allowed_domains = ['movie.movie-zeta.douban.com']
    start_urls = ['http://movie.douban.com/top250/']
    
    rules = (
             Rule(SgmlLinkExtractor(allow = 'movie\.movie-zeta\.douban\.com/subject/\d+/$'),
                  'parse_movies',follow = True,
                  ),
             )
    
    def parse_movies(self,response):
        sel = Selector(response)
        
        item = DoubanItem()
        item['title'] = sel.xpath('//h1/span[@property="v:itemreviewed"]/text()').extract()
        yield item