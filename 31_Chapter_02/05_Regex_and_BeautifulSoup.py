from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('https://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html, 'html.parser')

# Pass a regex as an argument to Beautiful Soup
images = bs.find_all('img', {'src': re.compile(r'../img/gifts/img.*\.jpg')})

for image in images:
    print(image['src'])

print("\n\n")

# Inserting a regex argument in the search for the tag
images = bs.find_all(re.compile(r'im.'))
for image in images:
    print(image['src'])