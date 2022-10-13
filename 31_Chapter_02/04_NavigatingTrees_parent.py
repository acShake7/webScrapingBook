from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html, 'html.parser')

# tag here is the tag object for the specific img
tag = bs.find('img', {'src':'../img/gifts/img1.jpg'})

# Now we navigate to its parent and then to that parents previous sibling
# which happens to be the column with the price of that product / image
print(tag.parent.previous_sibling.get_text())


