'''
A Softer Side
Ver: 0.1
'''

# Import Packages
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup
import re


# This is the link to the archives
link = 'https://www.asofterworld.com/archive.php'


# Function to get the HTML from the link + Erro checking for URLError & HTTPError
def get_html(link):
    '''
    This function takes in a url. Then it requests the data from the url.
    If it works it returns the html data.
    If not, it checks for HTTP and URL errors
    '''
    try:
        html = urlopen(link)
    except HTTPError as e1:
        print("*** WARNING ***\nHTTPError thrown: File does not exist or corrupted\nError Message is ....")
        print(e1)
        return None
    except URLError as e2:
        print("*** WARNING ***\nURLError thrown: Server down or doesnt exist\nError Message is ....")
        print(e2)
        return None
    else:
        return html




# Get HTML
html = get_html(link)

'''
ACCESSING THE BEAUTIFUL SOUP OBJECT AND THE TAG SHOULD THEN GET PUSHED
TO A FUNCTION AND GET CHECKED FOR ATTRIBUTE ERROR 
Perhaps one for grabbing the A tags from the links
Perhaps one for chasing the link and getting the next page HTML (which 
should also go through the HTMLError and URLError) and then grab the title
text and the image src link (and again check for the ATTRIBUTE ERROR). 
Do a killer way to the club these 2 funcions if you can!
'''

bs = BeautifulSoup(html, 'html.parser')

# Searching by style - this works
# nameList = bs.table.find_all('a', {'style':'text-decoration:underline'})

# Searching by regex of the href
# in the link 'php?id' was the problem cause the ? was being interreted as an optional. Had to use the escape sequence '\?'
nameList = bs.table.find_all('a', {'href': re.compile(r'http://www.asofterworld.com/index.php\?id=\d+')})

# Check to see how many image links were found and physically check 
# on the webpage that number is the same - should be 1248
print(len(nameList)) # should be 1248


for navlink in nameList[:5]:
    print(navlink)
