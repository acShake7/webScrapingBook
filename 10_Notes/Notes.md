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

>><p style="color:red;">Put a table here to see what parsers are available</p>


<br>
---

