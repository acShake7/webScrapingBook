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

4. Set a time delay so you arent taxing the server.

5. Working in a list is mental. Need to convert it to a file on your drive so that you dont have to
    keep querying the server for the same info.

6. Saving the images - remember to append the index number to the filename so you have an order to it.

7. Database solution to the lists and the images.

****************************************
'''

# Import Packages

from bs4 import BeautifulSoup
import re

# My custom packages
import helper_Functions

# This is the link to the archives
link = 'https://www.asofterworld.com/archive.php'

# Get HTML
html = helper_Functions.get_html(link)

# Check that html is not a None Object
helper_Functions.if_HtmlNoneTerminate(html)

bs = BeautifulSoup(html, 'html.parser')


# Searching by regex of the href
# in the link 'php?id' was the problem cause the ? was being interreted as an optional. Had to use the escape sequence '\?'
tagList = bs.table.find_all('a', {'href': re.compile(r'http://www.asofterworld.com/index.php\?id=\d+')})

# Check to see how many image links were found and physically check 
# on the webpage that number is the same - should be 1248
print("\nNumber of links found = " + str(len(tagList))) # should be 1248
print("Sanity Check - Number of Links - should be 1248.\n\n")

# Lists to populate the link to the image page, the title text, and eventually the link to the image.
pageList = []
titleTextList = []
imageSrcList = []

# populating the lists with the link and the title text
# PS!!!! IMPORTANT - I AM ONLY SCRAPING 5 IMAGES. ONCE THE CODE IS SET I WILL SCRAPE THE REST. CHANGE THE RANGE BELOW WHEN YOU ARE READY TO DO SO!
for link in tagList[0:5]:
    titleTextList.append(link.get_text())
    pageList.append(link.attrs['href'])

    # Following the link to get the HTML
    pageLinkHTML = helper_Functions.get_html(link=link.attrs['href'])

    if pageLinkHTML == None:
        # Log the broken link: 
        # TO DO - Here I am printing. But when live I need to log it into a proper Log that i can check at the end of the scrape.
        print("\n ** WARNING ** - Link broken : @ index" + str(tagList.index(link)) + " - Link - " + link.attrs['href'])
        imageSrcList.append(None)
    else:
        bs = BeautifulSoup(pageLinkHTML, 'html.parser')

        imgTag = helper_Functions.get_img_tag(bs)
        if imgTag == None:
            print("\n ** WARNING ** - Attribute error\n")
            imageSrcList.append(None)
        else:
            # SANITY : Title check
            print(link.get_text() == imgTag.attrs['title'])
        
            # Add the image src to the list
            imageSrcList.append(imgTag.attrs['src'])
    # Now imgSrc is an ordered list with the links to all the images. None objects where there were broken links or Attribute errors.

# Sanity Check (checking 5) - works
for i in range(0,5):
    print(pageList[i] + " - " + titleTextList[i] + " - " + imageSrcList[i])

