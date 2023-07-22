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


class Question(Item):
    question = Field()
    description = Field()



class StackoverflowSpider(Spider):
    name = "myFirstSpider"