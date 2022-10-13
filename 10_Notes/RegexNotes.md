# Regex Notes

><p style="color:red;">TO DO > Notes for Regex - merge from Web Scraping book and Automate the Boring Stuff book. </p>


><p style="color:red;">Also for now, I have just the regex bit. I need to actually do the whole process. creatign the regex object, matching it, parsing, etc... Right now I am doing it just from the POV of pairing it with BeautifulSoup where it has a different mechanism of matching. </p>

<br>

## `re` package

All the regex (short for Regular Expressions) are in the `re` module
> \>\> import re

<br>

# Creating a Regex object by compiling it
Passing a string value representing a Regex expression to `re.compile()` returns a 'Regex pattern object' (or simply a 'regex object')

> phoneNum_Regex_Obj = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

Note: Putting r in front of the string above, marks the string as a 'raw string' [kinda like what you see is what you get, without the need for escape chatacters like \\n or \\\n]

<br>

# Matching Regex objects

A Regex object's `search()` method searches the string that is passed to it and for any matches to the regex pattern.

The `search()` method returns `None` if the regex pattern is not found in the string.

If the pattern is found, the `search()` method returns a `Match` object. `Match` object have a `group()` method that will return the actual matched text from the searched string.


```
import re

phoneNum_Regex_object = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

matched_obj = phoneNum_Regex_object.search("My phone number is 520-567-3458. Call me!")

print("Phone number found is: " + matched_obj.group())
```

## Recap : Steps in Finding a String Regex pattern

1. Import the `re` module
2. Create a regex object with `re.compile()`. *(P.S. use raw strings)*
3. Pass the string you want to search to the regex object's `search()` method. This returns a `Match` object.
4. Call the  `Match` object's `group()` method to retun a string of the actual matched text.

<br><br>

## Grouping with Parantheses
Adding parantheses ( ) will create groups in the regex.

For e.g. (\d\d\d)-(\d\d\d-\d\d\d\d) will create 2 groups in this phone number - one for the area code and the latter for the actual number.

Use the `group()` or `groups()` methods to access the matched groups or the entire string. `groups()` methods returns a tuple of multiple values (the matched groupings)
Usage in the code example below:

```
phoneNum_Regex_object = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
matched_obj = phoneNum_Regex_object.search("My phone number is 520-567-3458.")

print(matched_obj.group())
>> 520-567-3458

print( matched_obj.group(0))
>> 520-567-3458

print(matched_obj.group(1))
>> 520

print(matched_obj.group(2))
>> 567-3458

print(matched_obj.groups())
>> ('520', '567-3458')
```

<br><br>

## The `findall()` method
While `search()` will return a Match object of the first matched text in the searched string, the `findall()` method will return the strings of *"EVERY"* match in the searched string.

<br>

The `findall()` method does not return a `Match` object but a list of strings  - *as long as there are no groups in the regular expression*.

```
>> textToSearch = "Cell = 415-456-7896 and Mobile = 567-674-2398"
>> phoneNum_Regex_object = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
>> phoneNum_Regex_object.findall(textToSearch)
['415-456-7896', '567-674-2398']
```
<br>

If there are groups in the regular expression, then `findall()` will return a list of tuples.  Each item in the list is in a occurance of the matched string and in each item there is a tuple representing the groups of matched strings.

```
>>textToSearch = "Cell = 415-456-7896 and Mobile = 567-674-2398"
>> phoneNum_Regex_object = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
>> phoneNum_Regex_object.findall(textToSearch)
[('415', '456-7896'), ('567', '674-2398')]
```
<br>

---
<br>

# Character Class
<table>
    <tr>
        <th>Character class</th>
        <th>that represents</th>
    </tr>
    <tr>
        <td>\d</td>
        <td>Any numeric digit from 0 to 9</td>
    </tr>
    <tr>
        <td>\D</td>
        <td>Any character that is not a numeric digit from 0 to 9</td>
    </tr>
    <tr>
        <td>\w</td>
        <td>Any letter, numeric digit, or the underscore character</td>
    </tr>
    <tr>
        <td>\W</td>
        <td>Any character that is NOT a letter, numeric digit, or the underscore character</td>
    </tr>
    <tr>
        <td>\s</td>
        <td>Any space, tab, or new line</td>
    </tr>
    <tr>
        <td>\S</td>
        <td>Any character that is NOT a space, tab, or new line</td>
    </tr>
</table>

```
>> xmasRegex = re.compile(r'\d+\s\w+')
>> xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')

['12 drummers', '11 pipers', '10 lords', '9 ladies', '8 maids', '7 swans', '6 geese', '5 rings', '4 birds', '3 hens', '2 doves', '1 partridge']
```

## Making your own Character Classes

><p style="color:red;">STOPPED HERE - RESUME FROM HERE</p>


<br><br><br><br><br>

a* - 0 or more

(cc)* - can be grouped - 'cc' 0 or more times. basically even times.

|
(d|e) - this thing or that thing - d or e
batRegex = re.compil(r'Bat(man|mobile|copter|woman)')

? - optional - sometimes you want to match a pattern optinally. i.e. the regex should find a match wether or not that bit of text is there. The `?` character flags the group that preceeds it to be an optional part of the pattern.
batRegex = re.compil(r'Bat(wo)?man') # this will return both Batman or Batwoman

\+ 1 or more times

[ ] - matches any character within the brackets

( ) - grouped sub expression. can be static like (cc)* or more flexible like (b*a)+

{m} - specific numer of repetitions m times. 

{m,n} - matches the preceeding character, subexpression or bracketed character between m & n times (inclusive). Can also be unbounded e.g. {m,} is m times or more. or {,n} is repetion upto m times including 0 times.

Greedy & Non-Greedy matching.
> (Ha){3,5}

`group()` returns the most number of Ha's it can grab. so if it can grab 3,4 or 5 - it will go for 5. This is `greedy` and it is the default. i.e. it will match with the longest possible string possible even thought the shorter versions are also valid and satify the regex pattern. 

The non-greedy version of the curly brackets { }, i.e. matches the smallest string possible, has the closing curly bracket followed by a question mark (?)
> (Ha){3,5}? 





a{2,3}b{2,3} = aabbb, aaabbb, aabb, ...

[^] - matches any single character that is not in the bracket. e.g. [^A-Z]* ... e.g. apple, lowercase, querty

.

^ - indicates that a character or subexpression occurs at the beginning of a string

\ - escape character

$

?! - does not contain



<table>
    <tr>
        <td>hellow</td>
        <td>hellow</td>
        <td>hellow this is who i am and this is very cool</td>
    </tr>
    <tr>
        <td>hellow</td>
        <td>hellow</td>
        <td>hellow this is who i am and this is very cool</td>
    </tr>
    <tr>
        <td>hellow</td>
        <td>hellow</td>
        <td>hellow this is who i am and this is very cool</td>
    </tr>

</table>