# Regex Notes

><p style="color:red;">TO DO > Notes for Regex - merge from Web Scraping book and Automate the Boring Stuff book. </p>


><p style="color:red;">Also for now, I have just the regex bit. I need to actually do the whole process. creatign the regex object, matching it, parsing, etc... Right now I am doing it just from the POV of pairing it with BeautifulSoup where it has a different mechanism of matching. </p>

a* - 0 or more

(cc)* - can be grouped - 'cc' 0 or more times. basically even times.

|
(d|e) - this thing or that thing - d or e

\+ 1 or more times

[ ] - matches any character within the brackets

( ) - grouped sub expression. can be static like (cc)* or more flexible like (b*a)+

{m,n} - matches the preceeding character, subexpression or bracketed character between m & n times (inclusive).

a{2,3}b{2,3} = aabbb, aaabbb, aabb, ...

[^] - matches any single character that is not in the bracket. e.g. [^A-Z]* ... e.g. apple, lowercase, querty

.

^ - indicates that a character or subexpression occurs at the beginning of a string

\ - escape character

$

?! - does not contain

