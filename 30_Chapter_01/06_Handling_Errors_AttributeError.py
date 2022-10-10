from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://pythonscraping.com/pages/page1.html')
bs = BeautifulSoup(html, 'html.parser')

try:
    badContent = bs.TagThatDoesNotExist.anotherTag
    # badContent = bs.h1 (This should work)

    # PS - remember that 'bs.TagThatDoesNotExist' returns a None object > you need to check for this
    # Also, 'bs.TagThatDoesNotExist.anotherTag' is looking for 'anotherTag' on a None object - this is what raises the AttributeError 
except AttributeError as e:
    print(e)
    print("Tag was not found")
else:
    if badContent == None:
        print('Tag was not found')
    else:
        print(badContent)
