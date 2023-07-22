"""
 WEB SCRAPING - Wikipedia

    First practice of web scraping.
    Tools:
        - Request.
        - lxml.

"""



import requests
from lxml import html



Headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"}

URL = "https://www.wikipedia.org"

Response = requests.get(URL,headers= Headers)

parser = html.fromstring(Response.text)
print(type(parser))

#Practice 1.
#extract info from that TAG.
print(parser.get_element_by_id("js-link-box-en").text_content())



#Practice 2.
#extract info using XPATH.
print(parser.xpath("//a[@id='js-link-box-en']/strong/text()"))



#Practice 3.
#extract all languages from the wikipedia main page.
print(parser.xpath("//div[contains(@class, 'central-featured-lang')]//strong/text()"))

Languages = parser.find_class("central-featured-lang")
for lang in Languages: print(lang.text_content())


