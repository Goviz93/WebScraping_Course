"""
 WEB SCRAPING - Stackoverflow

    Second practice of web scraping.
    Tools:
        - Request.
        - Beautifulsoup.

"""


import requests
from bs4 import BeautifulSoup



Headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"}

URL = "https://stackoverflow.com/questions/"

Response = requests.get(URL,headers= Headers)

soup = BeautifulSoup(Response.text, 'lxml')

#Find the main container with all the questions.
questionContainer = soup.find(id='questions')

#Find all questions
questionList = soup.find_all('div', class_= 's-post-summary')

#Extract data from every single question.
for question in questionList:
    print(f"Title -> {question.find('h3').text.strip()}")
    des = question.find(class_ = 's-post-summary--content-excerpt').text
    print(f"Description -> {des.strip()}")

    #Second way to find the same information.
    des2 = question.find('h3').find_next_sibling('div').text
    print(f"Description -> {des2.strip()}\n")