"""
 WEB SCRAPING - Stackoverflow

    Second practice of web scraping.
    Tools:
        - Request.
        - Beautifulsoup.

"""


from scrapy import Field
from scrapy.item import Item
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.loader import ItemLoader
from scrapy.crawler import CrawlerProcess


class Question(Item):
    question = Field()
    #description = Field()



class StackoverflowSpider(Spider):
    name = "myFirstSpider"
    Headers = {"USER_AGENT": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"}
    startURLS = ['https://stackoverflow.com/questions']

    def parse(self, response,):
        sel = Selector(response)
        #Using a xpath:
        #questionList = sel.xpath('//div[@id="questions"]//div[contains(@class, "s-post-summary    js-post-summary)"]')
        questionList = sel.xpath('//div[@id="questions"]/div[@class="s-post-summary    js-post-summary"]')

        for obj in questionList:
            item = ItemLoader(Question(), obj)
            item.add_xpath('question', './/h3/a/text()')
            #item.add_xpath('description', './/div[@class="s-post-summary--content-excerpt"]/text()')

            yield item.load_item()


#Command to run this in the terminal:
#   scrapy runspider 3_Stackoverflow.py -O data.csv:csv

"""
process = CrawlerProcess({
    'FEED_FORMAT': 'csv', # Formato del archivo para guardar los datos
    'FEED_URI': 'data.csv' # Nombre del archivo para guardar los datos
})
process.crawl(StackoverflowSpider) # Nombre de la clase de tu Spider
process.start()
"""


