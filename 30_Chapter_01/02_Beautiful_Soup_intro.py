from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://pythonscraping.com/pages/page1.html')

bs = BeautifulSoup(html.read(), 'html.parser')

print(bs.h1)
# Note: this returns only the first instance of the H1 tag found on the page.

