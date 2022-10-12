from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html, 'html.parser')

# This outputs all the rows of the products from the product table
# except for the first row (the title row)
for sibling in bs.find('table', {'id':'giftList'}).tr.next_siblings:
    print(sibling)

# This block chooses a row in the middle of the product row/list and 
# find the next siblings from there down
# for sibling in bs.find('tr', {'id':'gift3'}).next_siblings:
#     print(sibling)

# This block chooses a row in the middle of the product row/list and 
# find the previous siblings from there up including the table head
# for sibling in bs.find('tr', {'id':'gift3'}).previous_siblings:
#     print(sibling)


'''
Instead of this:
bs.find('table', {'id':'giftList'}).tr

you could have also navigated to the same point by either of the options below:
   bs.table.tr 
   bs.tr

But it is good to be specific to use the table id or other uniquely characteristic 
defining features to make the code robust in case the web page changes in the future.
It will not break your code.

'''