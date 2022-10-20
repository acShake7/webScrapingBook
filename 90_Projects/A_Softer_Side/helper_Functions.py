'''
These are the helper functions for the Softer Side project
'''

# Import packages
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup


# Function to get the HTML from the link + Error checking for URLError & HTTPError
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



# Check if html is a None Object (meaning get_html func threw up URLError or HTTPError) and will terminate if it is.
# Use this only for the main starting point link - something is very wrong if the list of links is down and program should terminate.
def if_HtmlNoneTerminate(html):
    if html == None:
        print("\nError was found. Program will terminate.\n")
        quit     # Is this the right way to break out of program execution? Is there a better way?



# Access the tag that contains the image
def get_img_tag(bs):
    try:
        imgTag = bs.find('div', id='comicimg').img

    except AttributeError as e:
        print('AttributeError thrown and caught - tag does not exist')
        print(e)
        return None
    else:
        if imgTag == None:
            print('Tag does not exist - None object generated')
            return None
        else:
            return imgTag