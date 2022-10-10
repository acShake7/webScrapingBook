from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bs = BeautifulSoup(html, 'html.parser')

# The characters in this HTML data/screenplay are all styled by CSS to be of span class=green. This makes it trivial to extract all the characters in the play.
nameList = bs.find_all('span', {'class':'green'})

for name in nameList:
    print(name.get_text())