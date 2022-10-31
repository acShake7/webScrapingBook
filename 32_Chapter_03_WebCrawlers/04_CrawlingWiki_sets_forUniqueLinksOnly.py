'''
Six degrees of separation from Kevin Bacon

This uses sets to keep only the unique links (i.e. avoid repeatedly scraping pages)

All the links reside inside the div tag with the id set to bodyContent

the URLs begin with /wiki/

single function - getLinks (takes in a wiki link in the form /wiki/ArticleName and gets all the links of the same form on that page)
A main function that calls getLinks with a starting article and then choosing a random article from the list of URLs returned and repeats
the process till you stop the program or no more article links are found on that page

What is missing from this program: handling exceptions - URL, HTTP and Attribute errors
'''


from hashlib import new
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()   # empty set

def getLinks(pageURL):
    global pages    # to enable you to modify the global variable pages inside this function
    html = urlopen('http://en.wikipedia.org{}'.format(pageURL))
    bs = BeautifulSoup(html, 'html.parser')
    
    for link in bs.find_all('a', href = re.compile('^(/wiki/)')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                # we have encountered a new page
                newPage = link.attrs['href']
                print(newPage)
                pages.add(newPage)
                getLinks(newPage)


getLinks("")