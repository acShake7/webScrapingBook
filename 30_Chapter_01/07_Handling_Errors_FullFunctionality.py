'''
    ******
This program does a full functionality walkthough of taking a url,
grabbing the HTML (while checking for server errors and files missing),
then accesses a tag's content (while checking it that tag does indeed exist)

Can use this code ready to bake - as I have defined the functionality into 2 neat functions.
    ******
'''

# Import all packages
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup


def returnHTML(url):
    '''
    This function takes in a url. Then it requests the data from the url.
    If it works it returns the html data.
    If not, it checks for HTTP and URL errors
    '''
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
        print("HTTPError caught: File not found.")
        return None

    except URLError as e:
        print(e)
        print("URLError caught - Server does not exist or is down.")
        return None

    else:
        return html


def accessTag(html):
    '''
    This function takes in the html and uses BeautifulSoup to access tags in it.
    If the tag does not exist, this function will check for it and also guard ...
    ...against any AttributeError that is thrown when accessing a tag on a None object
    '''
    bs = BeautifulSoup(html, 'html.parser')
    try:
        # tagContent = bs.body.h1 # This should work
        tagContent = bs.body1.h4
    except AttributeError as e:
        print(e)
        print('AttributeError thrown and caught - tag does not exist')
        return None
    else:
        if tagContent==None:
            print('Tag does not exist - None object generated')
            return None
        else:
            return tagContent


url = "http://pythonscraping.com/pages/page1.html"
html = returnHTML(url)
if html == None:
    print("No HTML returned due to the Error")
else:
    tagContent = accessTag(html)
    if tagContent==None:
        print('Content is None as the Tag did not exist. Try again with a tag that exists.')
    else:
        print(tagContent)

