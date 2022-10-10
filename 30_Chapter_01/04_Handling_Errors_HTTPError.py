from urllib.request import urlopen
from urllib.error import HTTPError

from bs4 import BeautifulSoup

try:
    # in the weblink below page1.html exists & works.
    html = urlopen('http://pythonscraping.com/pages/page15.html')
except HTTPError as e:
    print(e)
    # return null, break or Plan B actions if this error is returned.
else:
    bs = BeautifulSoup(html, 'html.parser')
    print(bs.h1)