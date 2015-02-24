#This Spider is created to scrap the data off the webpage. This is later stored in a JSON file

from scrapy.spider import Spider
from scrapy.selector import Selector
from ucrawler.items import UcrawlerItem



class MySpider(Spider):
      name='udacity'
      allowed_domains=['udacity.com']
      start_urls=['https://www.udacity.com/courses#!/all']
      
      
      def parse(self, response):
        
        
        sel=Selector(response)
        blocks=[]
        block=UcrawlerItem()
        
        block['title']=sel.xpath('//h2/a/text()').extract()
        block['link']=sel.xpath('//h2/a/@href').extract()
        for i in range(1,66):
        
          block['about']=sel.xpath('//p[1]/text()').extract()
          block['desc']=sel.xpath('//p[2]/text()').extract()
          block['level']=sel.xpath('//p[3]/text()').extract()
        
        blocks.append(block)
        
        return blocks
