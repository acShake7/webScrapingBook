'''
Six degrees of separation from Kevin Bacon
Finding all the links on his Wiki page
'''

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://en.wikipedia.org/wiki/Kevin_Bacon')
bs = BeautifulSoup(html, 'html.parser')

a=0
for link in bs.find('div', id="bodyContent").find_all('a'):
    if 'href' in link.attrs:
        print(link)
        a+=1

print(a)