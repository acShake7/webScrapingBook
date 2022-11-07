'''
Refactored ode for a web crawler that gets both the internal and external url links

This collects a list of all the external and internal links found on the site

I've take the code from 06_Full_ScrapingCode_internal_n_ExternalURL.py as the starting point and reused the functions to achieve this.
The power of reusability.

What has not been included but should be:
Handling errors  - HTTPError, URLError, AttributeError

'''

# Import Packages
from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re
import datetime
import random

random.seed(datetime.datetime.now())        # seeding the random generator

pages = set()

# Retrieve a list of all interal links found on a page
def getInternalLinks(bs, includeURL):
    includeURL='{}://{}'.format(urlparse(includeURL).scheme, urlparse(includeURL).netloc)   # Dissect this!
    internalLinks = []
    # Find all the links that begin with a "/"
    for link in bs.find_all('a', href=re.compile('^(/|.*'+includeURL+')')):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                if link.attrs['href'].startswith('/'):
                    internalLinks.append(includeURL+link.attrs['href'])
                else:
                    internalLinks.append(link.attrs['href'])
    return internalLinks

# Retrieve a list of all external links found on a page
def getExternalLinks(bs, excludeURL):
    externalLinks=[]
    # Find all the links that begin with 'http' or 'www' that do not contain the URL
    for link in bs.find_all('a', href=re.compile('^(http|www)((?!'+excludeURL+').)*$')):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks

def getRandomExternalLink(startingPage):
    html = urlopen(startingPage)
    bs = BeautifulSoup(html, 'html.parser')
    externalLinks = getExternalLinks(bs, urlparse(startingPage).netloc)
    if len(externalLinks) == 0:
        print('No external links, looking around the site for one')
        domain = '{}://{}'.format(urlparse(startingPage).scheme, urlparse(startingPage).netloc)
        internalLinks = getInternalLinks(bs, domain)
        return getRandomExternalLink(internalLinks[random.randint(0, len(internalLinks)-1)])
    else:
        return externalLinks[random.randint(0, len(externalLinks)-1)]

def followExternalOnly(startingSite):
    externalLink = getRandomExternalLink(startingSite)
    print("Random external link is : {}".format(externalLink))
    followExternalOnly(externalLink)

allExternalLinks = set()
allInternalLinks = set()

def getAllExternalLinks(siteURL):
    html = urlopen(siteURL)
    domain = '{}://{}'.format(urlparse(siteURL).scheme, urlparse(siteURL).netloc)
    bs = BeautifulSoup(html, 'html.parser')
    internalLinks = getInternalLinks(bs, domain)
    externalLinks = getExternalLinks(bs, domain)

    for link in externalLinks:
        if link not in allExternalLinks:
            allExternalLinks.add(link)
            print(link)
    
    for link in internalLinks:
        if link not in allInternalLinks:
            allInternalLinks.add(link)
            print(link)

allInternalLinks.add('https://www.politico.com')
getAllExternalLinks('https://www.politico.com')

# 'https://edition.cnn.com'
# 'http://oreilly.com'