# Regex Notes

Python Regex Documentation <a href="https://docs.python.org/3/library/re.html">docs.python.org</a>
> A lot more here. Wow!

> Also look at this link: Prety neat tutorial from Real Python : https://realpython.com/regex-python/

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
<br>

---

<br><br>

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

You can define your own character class using square brackets [ ]

For e.g. the character class [aeiouAEIOU] will match any vowel upper or lower case.

```
>> vowel_Regex = re.compile(r'[aeiouAEIOU]')
>> vowel_Regex.findall("Pick all the VOWELS!")
['i', 'a', 'e', 'O', 'E']
```

You can also include a **range of numbers or letters** by using a hyphen (-). e.g. [a-zA-Z0-9] will match all lower case and uper case letter and numbers.

> Note that inside the square brackets, the normal regular expression symbols are not interpreted as such. This means you do not need to escape the ., *, ?, or () characters with a preceding backslash. <br>For example, the character class [0-5.] will match digits 0 to 5 and a period. You do not need to write it as [0-5\.]

<br>

### Negative Character Set
By placing a caret (^) just after the charcter class's opening square bracket, you can make a *negative charracter class* - i.e. it will match everything not in the character class. 

```
>> vowel_Regex = re.compile(r'[^aeiouAEIOU]')
>> vowel_Regex.findall("DONT Pick all the VOWELS!")
['D', 'N', 'T', ' ', 'P', 'c', 'k', ' ', 'l', 'l', ' ', 't', 'h', ' ', 'V', 'W', 'L', 'S', '!']
```

<br><br>

## Start and End of Searched Text
`^` at the start of a regex to indicate that a match MUST occur at the beginning of the searched text.

`$` at the end of a regex to indicate that the searched string MUST end with this regex pattern.

You can use the `^` and `$` to indicate that the entire searched string must match the regex.

```
>> begins_With_Hello = re.compile(r'^Hello')
>> begins_With_Hello.search("Hello friend!")
<re.Match object; span=(0, 5), match='Hello'>

>> begins_With_Hello.search("Hi and Hello friend!") == None
True
```

```
>> end_with_number = re.compile(r'\d$')
>> end_with_number.search("my age is 42")
<re.Match object; span=(11, 12), match='2'>
```

```
>> whole_string_is_num = re.compile(r'^\d+$')
>> whole_string_is_num.search("12345678")
<re.Match object; span=(0, 8), match='12345678'>

>> whole_string_is_num.search("12xc34") == None
True
```
<br><br>

## Matching Everything with Dot-Star (`.*`)

Sometimes you want to match everything and anything.

```
>> nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
>> mo = nameRegex.search("First Name: Al Last Name: Jones")

>> mo.group()
First Name: Al Last Name: Jones

>> mo.group(1)
Al

>> mo.group(2)
Jones
```

`.*` uses greedy mode and tries to grab as much as possible. To use non-greedy mode use `.*?`

```
>> non_greedy_regex = re.compile(r'<.*?>')
>> mo = non_greedy_regex.search("<To serve man> for dinner>")
>> mo.group()
<To serve man>


>> greedy_regex = re.compile(r'<.*>')
>> mo = greedy_regex.search("<To serve man> for dinner>")
>> mo.group()
<To serve man> for dinner>
```
<br><br>

## Matching New Lines with the Dot character

`.*` will match everything except a newline.

By passing `re.DOTALL` as the second argument to `re.compile()`, you can make the dot character (.) match *ALL* characters including the newline character (\n).

```
>> noNewLineRegex = re.compile(r'.*')
>> noNewLineRegex.search("First line.\nSecond line.").group()
First line.

>> NewLineRegex = re.compile(r'.*', re.DOTALL)
>> NewLineRegex.search("First line.\nSecond line.").group()
First line.
Second line.
```

<br>

## Case-Insensitive Matching

`re.compile(r'RoboCop')` and `re.compile(r'robocop')` match different strings.

If you dont care about case then pass `re.I` or `re.IGNORECASE` as the second argument to `re.compile()`

`re.compile(r'robocop', re.IGNORECASE)` will now match any of these - RoboCop, robocop, roboCOP, ...

<br>

## Substituting strings with the `sub()` method

Regex can not only find text patterns but can also find and substitute new text in place of those patterns. 

The `sub()` method for Regex objects is passed two arguments. The first argument is a string to replace any matches. The second is the string for the regular expression. The `sub()` method returns a string with the substitutions applied.

```
>> namesRegex = re.compile(r'Agent \w+')
>> namesRegex.sub("CENSORED", "Agent Alice gave secret docs to Agent Bob.")
CENSORED gave secret docs to CENSORED.
```

<br>
Sometimes you may need to use the matched text itself as part of the substitution. In the first argument to `sub()`, you can type \1, \2, \3, and so on, to mean “Enter the text of group 1, 2, 3, and so on, in the substitution.”


```
>> namesRegex = re.compile(r'Agent (\w)\w*')
>> namesRegex.sub(r'\1****', "Agent Alice gave secret docs to Agent Bob when she saw Agent Paul.")
A**** gave secret docs to B**** when she saw P****.
```

The `\1` in that string will be replaced by whatever text was matched by group 1—that is, the (`\w`) group of the regular expression.

<br><br>

## VERBOSE Mode

Matching complicated text patterns might require long, convoluted regular expressions. You can mitigate this by telling the `re.compile()` function to ignore whitespace and comments inside the regular expression string. This “verbose mode” can be enabled by passing the varible `re.VERBOSE` as the second argument to `re.compile()`.


So this long complicated regex below can be reframed.
```
phoneRegex = re.compile(r'((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}(\s*(ext|x|ext.)\s*\d{2,5})?)')
```

It can be reframed as :

```
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?            # area code
    (\s|-|\.)?                    # separator
    \d{3}                         # first 3 digits
    (\s|-|\.)                     # separator
    \d{4}                         # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?  # extension
    )''', re.VERBOSE)
```

Note that this previous code uses the triple quotes syntax (''') to create a multi-line string so that you can spread the regex definition over multiple lines and more comments (phython rules) to make it more legible.

<br><br>

## Combining arguments for `re.compile()`

Unfortunately, the re.compile() function takes only a single value as its second argument. You can get around this limitation by combining the `re.IGNORECASE`, `re.DOTALL`, and `re.VERBOSE` variables using the pipe character (`|`), which in this context is known as the *bitwise or* operator.

```
someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)
```






---
<br><br>

# Review of Regex Symbols

### `?` Optional
`?` - optional - sometimes you want to match a pattern optinally. i.e. the regex should find a match wether or not that bit of text is there.

The `?` character flags the group that preceeds it to be an optional part of the pattern. In other words, it matches it 0 or once.

```
batRegex = re.compil(r'Bat(wo)?man')

# this will return both Batman or Batwoman
```

### `.` Wildcard
`.` - is a wildcard character and will match any character except a newline. [to match an actual '.' use the escape sequence '\\.']

<br>

### `*` Zero or more
`*` - matches 0 or more fo the preceeding group
(cc)* - can be grouped - 'cc' 0 or more times. basically even times.

<br>

### `|` Or
(d|e) - this thing or that thing - d or e
```
batRegex = re.compil(r'Bat(man|mobile|copter|woman)')
```

<br>

### `+` 1 or more times
Matches the preceeding group 1 or more times.

<br>

### `{ }` repetitions

{m} - matches m specific repetitions of the preceeding group.

{m,n} - matches the preceeding character, subexpression or bracketed character between m & n times (inclusive). Can also be unbounded e.g. {m,} is m times or more. or {,n} is repetion upto m times including 0 times.

*Greedy & Non-Greedy matching.*
> (Ha){3,5}

`group()` returns the most number of Ha's it can grab. so if it can grab 3,4 or 5 - it will go for 5. This is `greedy` and it is the default. i.e. it will match with the longest possible string possible even thought the shorter versions are also valid and satify the regex pattern. 

The `non-greedy` version of the curly brackets { }, i.e. matches the smallest string possible, has the closing curly bracket followed by a question mark (`?`)
> (Ha){3,5}? 

<br>

### Specifying the Beginning and/or End of a String to Match
^spam - means that the string must begin with spam.

spam$ - means that the string must end with spam.


<br>

### `[ ]` Match any character betwen the bracekts

<br>

`[ ]` - matches any character within these brackets

`[^ ]` - match any character that isnt with these brackets

<br>

---
