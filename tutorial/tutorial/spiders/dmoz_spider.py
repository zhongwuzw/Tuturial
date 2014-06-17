#coding=utf8
from scrapy.spider import Spider
from scrapy.selector import Selector
from tutorial.items import DmozItem
from scrapy.http import Request
from scrapy.contrib.loader.processor import MapCompose

class DmozSpider(Spider):
    name = 'dmoz'
    allowed_domains = ["dmoz.org"]
    start_urls = [
                  "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
                  "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
                  ]
    
    def parse(self,response):
        sel = Selector(response)
        sites = sel.xpath('//ul/li')
       # items = []
        for site in sites:
            item = DmozItem()
            item['title'] = site.xpath('a/text()').extract()
            item['link'] = site.xpath('a/@href').extract()
            item['desc'] = site.xpath('text()').extract()
            yield item
        for url in sel.xpath('//a/@href').extract() :
            if not url.startswith('/'):
                yield Request(url,callback = self.parse)
            
        #    items.append(item)
     #   return items
    