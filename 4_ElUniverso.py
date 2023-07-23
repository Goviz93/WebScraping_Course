
"""
OBJETIVO:
    - Extraer los titulares y el resumen de las noticias en la pagina principal de deportes de EL UNIVERSO.
    - Contrastar el uso de Beautiful Soup y Scrapy para parsear el arbol HTML.
"""

from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.loader.processors import MapCompose
from scrapy.loader import ItemLoader
from bs4 import BeautifulSoup
from scrapy.crawler import CrawlerProcess


#Abstraccion de datos a extraer.
class Noticia(Item):
    id = Field()
    Titular = Field()
    Descripcion = Field()

#Clase Spider.
class ElUniversoSpider(Spider):
    name =  "SegundoSpider"
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36',
        # 'FEED_EXPORT_FIELDS': ['id', 'descripcion', 'titular'], # Como ordenar las columnas en el CSV?
        # 'CONCURRENT_REQUESTS': 1 # numero de requerimientos concurrentes
        #'FEED_EXPORT_ENCODING': 'utf-8'
    }
    start_urls = ['https://www.eluniverso.com/deportes/']

    def parse(self, response):
        sel = Selector(response)
        noticias = sel.xpath('//div[contains(@class, "content-feed")]/ul/li')
        for i, elem in enumerate(noticias):
            item = ItemLoader(Noticia(), elem)

            # Llenando mi item a traves de expresiones XPATH
            item.add_xpath('Titular', './/h2/a/text()')
            item.add_xpath('Descripcion', './/p/text()')
            item.add_value('id', i)
            yield item.load_item() # Retorno mi item lleno

# EJECUCION
# scrapy runspider 4_ElUniverso.py -o resultados.csv