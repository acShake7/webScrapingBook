from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup

try:
    html = urlopen('https://pythonscrapingthisurldoesnotexist.com')
    # http://pythonscraping.com/pages/page1.html - the page exists
    # http://pythonscraping.com/pages/page15.html - the page does not exist
    # https://pythonscrapingthisurldoesnotexist.com - The url does not exist
except HTTPError as e:
    print(e)
    print("Did not work - HTTPError")
except URLError as e:
    print(e)
    print("Did not work - URLError - The server could not be found!")
else:
    print("It worked")
    bs = BeautifulSoup(html, 'html.parser')
    print(bs.h1)
