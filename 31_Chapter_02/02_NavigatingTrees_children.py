from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html, 'html.parser')

# This will print the list of product rows in the giftList table
for child in bs.find('table', {'id':'giftList'}).children:
    print(child)

# This one on the other hand will print all the tags at each sub-nested-level 
# for child in bs.find('table', {'id':'giftList'}).descendants:
#     print(child)