'''
This program crawls Wikipedia and collects the title, the first para of content, and the link to edit the page.
'''

# Import packages
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()   # will store all the unique links found here

def getLinks(pageURL):
    global pages    # to enable you to modify the global variable pages inside this function

    html = urlopen('http://en.wikipedia.org{}'.format(pageURL))
    bs = BeautifulSoup(html, 'html.parser')

    try:
        print(bs.h1.get_text())                                                 # title text
        print(bs.find(id='mw-content-text').find_all('p')[1])                   # first para content
        print(bs.find(id='ca-edit').find('a').attrs['href'])       # page edit link
    
    except AttributeError as e:
        print('****** This page is missing something! Continuing ...')
    
    for link in bs.find_all('a', href=re.compile('^(/wiki/)')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                # we have encountered a new page
                newPage = link.attrs['href']
                print('-'*20)
                print(newPage)
                pages.add(newPage)
                getLinks(newPage)       # function calls itself to scrape the newly found link


getLinks('/wiki/Oliver_Stone')