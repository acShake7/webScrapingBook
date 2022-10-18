'''
A Softer Side
Ver: 0.1
'''

'''
****************************************
TO DO
1. the function defitions - make them into separate packages so that this is cleaner to read.

2. Once the get_html() returns make sure its not a None object. 
If it is, what then?
    - in the case of the Archive page, that is easy
    - in the case of one of the 1478 pages being returned there is a possiblity that one of
     those links might be corrupted or a trap to trip up the scraper. have to tackle this to be flagged
     and for the scraper to resume to the next link.

3. Define functions to access the tags (on Archive page and on each of the 1478 links) - If you can reuse
    function for the 2 cases that will be golden.
    Now, when you access those tags, you need a check for Attribute error (you dont right now)
    And then you need to see how you tackle the attribute error in both cases.

4. Working in a list is mental. Need to convert it to a file on your drive so that you dont have to
    keep querying the server for the same info.

5. Saving the images - remember to append the index number to the filename so you have an order to it.

6. Database solution to the lists and the images.

****************************************
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
NEED TO CHECK THAT THE HTML BEING RETURNED IS NOT None OBJECT (i.e one of the errors caught)
ACCESSING THE BEAUTIFUL SOUP OBJECT AND THE TAG SHOULD THEN GET PUSHED
TO A FUNCTION AND GET CHECKED FOR ATTRIBUTE ERROR 
Perhaps one for grabbing the A tags from the links
Perhaps one for chasing the link and getting the next page HTML (which 
should also go through the HTMLError and URLError) and then grab the title
text and the image src link (and again check for the ATTRIBUTE ERROR). 
Do a killer way to the club these 2 funcions if you can!
'''

bs = BeautifulSoup(html, 'html.parser')

# Approach 1: Searching by style - this works
# pageLinkList = bs.table.find_all('a', {'style':'text-decoration:underline'})

# Approach 2: Searching by regex of the href
# in the link 'php?id' was the problem cause the ? was being interreted as an optional. Had to use the escape sequence '\?'
tagList = bs.table.find_all('a', {'href': re.compile(r'http://www.asofterworld.com/index.php\?id=\d+')})

# Check to see how many image links were found and physically check 
# on the webpage that number is the same - should be 1248
print("\nNumber of links found = " + str(len(tagList))) # should be 1248
print("Sanity Check - Number of Links - should be 1248.\n\n")


# Check
# View a subset of the <a> tags thrown up...
# for navlink in pageLinkList[:5]:
#     print(navlink)

# Lists to populate the link to the image page, the title text, and eventually the link to the image.
pageList = []
titleTextList = []
imageSrc = []

# populating the lists with the link and the title text
# PS!!!! IMPORTANT - I AM ONLY SCRAPING 5 IMAGES. ONCE THE CODE IS SET I WILL SCRAPE THE REST. CHANGE THE RANGE BELOW WHEN YOU ARE READY TO DO SO!
for link in tagList[0:5]:
    titleTextList.append(link.get_text())
    pageList.append(link.attrs['href'])

    # Following the link to get the HTML
    pageLinkHTML = get_html(link=link.attrs['href'])
    bs = BeautifulSoup(pageLinkHTML, 'html.parser')
    # Access the tag that contains the image
    imgTag = bs.find('div', id='comicimg').img
    # SANITY : Title chech
    print(link.get_text() == imgTag.attrs['title'])
    
    # Add the image src to the list
    imageSrc.append(imgTag.attrs['src'])



# Sanity Check (checking 5) - works
# for i in range(0,5):
#     print(pageList[i])
#     print(titleTextList[i])
#     print(imageSrc[i])
