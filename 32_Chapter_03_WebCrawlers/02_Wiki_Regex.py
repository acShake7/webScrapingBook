'''
Six degrees of separation from Kevin Bacon
Using Regex

All the links reside inside the div tag with the id set to bodyContent
The URLs do not contain colons(:)
the URLs begin with /wiki/
'''

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('http://en.wikipedia.org/wiki/Kevin_Bacon')
bs = BeautifulSoup(html, 'html.parser')

a=0
for link in bs.find('div', {'id':'bodyContent'}).find_all('a', href=re.compile('^(/wiki/)((?!:).)*$')):
    if 'href' in link.attrs:
        print(link.attrs['href'])
        a+=1

print(a)
