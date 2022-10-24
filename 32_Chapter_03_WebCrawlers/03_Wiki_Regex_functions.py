'''
Six degrees of separation from Kevin Bacon

Using Regex

All the links reside inside the div tag with the id set to bodyContent
The URLs do not contain colons(:)
the URLs begin with /wiki/

single function - getLinks (takes in a wiki link in the form /wiki/ArticleName and gets all the links of the same form on that page)
A main function that calls getLinks with a starting article and then choosing a random article from the list of URLs returned and repeats
the process till you stop the program or no more article links are found on that page

What is missing from this program: handling exceptions - URL, HTTP and Attribute errors
'''

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random

random.seed(datetime.datetime.now())

# accepts a wiki link and returns all the article links from that page
def getLinks(articleURL):
    html = urlopen('http://en.wikipedia.org{}'.format(articleURL))
    bs = BeautifulSoup(html, 'html.parser')
    return bs.find('div', {'id':'bodyContent'}).find_all('a', href=re.compile('^(/wiki/)((?!:).)*$'))

links = getLinks('/wiki/Kevin_Bacon')

while len(links)>0:
    # Pick a random article from links and we will go down this route
    newArticle = links[random.randint(0,len(links)-1)].attrs['href']
    print(newArticle)
    links = getLinks(newArticle)

