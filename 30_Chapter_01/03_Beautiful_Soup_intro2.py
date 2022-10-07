from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://pythonscraping.com/pages/page1.html')

# BeautifulSoup can directly use the file object returned by urlopen without needing to call .read() first
bs1 = BeautifulSoup(html, 'html.parser')
print(bs1.h1)

# bs = BeautifulSoup(html.read(), 'html.parser')
# print(bs.h1)

