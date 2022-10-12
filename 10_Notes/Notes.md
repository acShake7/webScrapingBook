# Notes for Web Scraping

# Chapter 1 - Intro

<br>

## urllib
> Standard Python library to request data across the web, handling cookies, and changing metadata (such as headers and your user agent)

_**TO DO -**_ Browse documentation

```
from urllib.request import urlopen
html = urlopen('http://pythonscraping.com/pages/page1.html')
```
>><p style="color:red;">what type of object does this return</p>

<br>

---
<br>

## Beautiful Soup
```
from bs4 import BeautifulSoup
html = urlopen('http://pythonscraping.com/pages/page1.html')
bs = BeautifulSoup(html.read(), 'html.parser')

print(bs.h1)
```

**Only the first instance in returned**

The last line of the code block above `print(bs.h1)` returns only the first instance of the H1 tag found on the page.

In this case the H1 tag is nested inside a lot of other tags. And all of these are valid routes to get to it.

- bs.html.body.h1   // the full path
- bs.body.h1        // from bodythe first instance of h1
- bs.html.h1        // in the html tag the first instance of h1

<br><br>
Also BeautfulSoup can directly use the file object returned by urlopen without needing to call .read() first

```
bs1 = BeautifulSoup(html, 'html.parser')
print(bs1.h1)
```

<br>

### Parsers


- html.parser (built into python)
- lxml
- html5lib

```
bs = BeautifulSoup(html, 'html.parser')
bs = BeautifulSoup(html, 'lxml')
bs = BeautifulSoup(html, 'html5lib')
```
<br>

---

## Handling Exceptions

When you request data from a URL (using urlopen), 2 main things could go wrong:

1. The page is not found on the server (or there is an error retrieving it).

    A **HTTPError** will be returned - it may be a '404 Page Not Found' or '500 Internal Server Error' or so on.

2. The server is not found or the server is down.

    In this case a **URLError** is returned.

<br>

**NOTE:** The remote server is responsible for returning the HTTP status codes. So if the URL is down/non-existent, then the remote server will not be able to throw a HTTPError. The URLError must be caught.

<br>

### Problems with Tags - AttributeError

    If you attempt to access a tag that does not exist, BeautifulSoup will return a *None* object

    Now, if you try to access a tag on a *None* object, an **AttributeError** will be thrown.

Code Base to check for `HTTPError`, `URLError` and `AttributeError`:
```
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup


def returnHTML(url):
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
```
<br> <br>

---

# Chapter 2: Advanced HTML Parsing

## find() and find_all() with BeautifulSoup


find_all() - Finds all the tags on that page
find() - Finds the first instance of the tag on that page

<br>

> BeautifulSoup.find_all(tagName, tagAttribute, recursive, text, limit, keywords)
BeautifulSoup.find(tagName, tagAttribute, recursive, text, keywords)

<br>

**tagName** - you can pass a string name of a tag or even a Python list of string tag names.

**tagAttributes** - takes a Python dictionary of attributes and matches tags that contain any one of those attributes.

    bs.find_all('span', {'class':{'green','red'}})
    # finds all green and red span tags

**recursive** - boolean argument. How deep do you want to go? If True, then find_all will look into children and children's children and .... for tags that match your parameters. If set to False, it will look only at the top level tags in your document.

**text** - matches based on the text content of the tags, rather than the properties of the tags themselves.

**limit** - limits the search to the first 'x' items.

**keyword** - allows you to select tags that contain a particular attribute or set of attributes.

> bs.find_all(id='title', class_='text')

P.S. 'class' is a protected keyword in Python. The workaround in BeautifulSoup is to use 'class_'

<br>

### Using a list of arguments vs Keywords

The 2 lines below are identical:
```
bs.find_all(id='text')
bs.find_all('', {'id':'text'})
```
same for the 2 lines below
```
bs.find_all(class_='green')
bs.find_all('',{'class':'green'})
```

Passing a list of tags to bs.find_all() via the attributes list acts as an `or` filter [it selects a list of all tags that have tag1 or tag2 or tag3, ...]. If you have a lengthy list of tags you can end up with plenty that you dont want.

However, the `keyword` argument in bs.find_all() allows you to add an additional `and` filter to this. [e.g. bs.find_all(id='title', class_='text') finds a tag that has a title id **and** text class, **(not or)**.]

<br><br>

**Tag.get_text()**

    To get to the content in the tag. It strips all tags from the document and returns a Unicode string containing the text only.

    P.S. If you have nested tags like hyperlinks, span styles, etc.. they will all be stripped away.


## Other Beautiful Soup Objects

**BeauifulSoup objects**

    Instances seen in previous code examples as the variable 'bs'.

**Tag Objects**

    Retrieved in lists or individually by called find or find_all on a BeautifulSoup object, or drilling down (bs.div.h1)

**NavigableString Object**

    Used to represent text within tags, rather than the tags themselves.

**Comment Objects**

    Used to find HTML comments in comment tags, <!-- like this one-->

---

<br>

## Navigating Trees with Beautiful Soup

**Children** are exactly one tag below a parent.

**Descendants** can be at any level in the tree below a parent.

> All children are descendants BUT not all descendants are not children.

<br>
In general, BeautifulSoup functions always deal with the descendants of the current tag selected.

e.g. `bs.div.find_all('img')` will find the first `div` tag in the document, and then retrieve a list of all the `img` tags that are descendants of that `div` tag.

<br>

### Navigating to Children or Descendants
<br>

The `children()` and `descendants()` functions come in handy here.
```
# Children: This one will print all the children tags ONLY
for child in bs.find('table', {'id':'giftList'}).children:
    print(child)

# Descendants: This one on the other hand will print all the tags at each sub-nested-level 
for child in bs.find('table', {'id':'giftList'}).descendants:
    print(child)
```

<br>

### Navigating by Siblings
<br>

`next_siblings()` makes it trivial to collect data from tables especially ones with title rows.

```
# This outputs all the rows of the products from the product table except for the first row (the title row)

for sibling in bs.find('table', {'id':'giftList'}).tr.next_siblings:
    print(sibling)
```

Note: Objects cannot be siblings with themselves. So if you point BeautifulSoup to the table header row and from there use the `next_sibings()` function, it will return all the individual rows below (i.e. the ones at the same level in the table tree heirarchy)


The complement to `next_siblings()` is the `previous_siblings()` function.

`next_sibling()` and `previous_sibling()` perform similarly except for returning just a single tag rather than a list of them.


<br>

### Navigating by Parents
<br>
