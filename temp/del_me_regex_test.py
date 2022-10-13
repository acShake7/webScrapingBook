from cgitb import text
from nis import match
import re



# matched_obj = phoneNum_Regex_object.search("My phone number is 520-567-3458. Call me!")
# print("Phone number found is: " + matched_obj.group())
# print("Same Phone number found is: " + matched_obj.group(0))
# print("Area code is: " + matched_obj.group(1))
# print("Actual phone number is: " + matched_obj.group(2))
# print("All the groups:")
# print(matched_obj.groups())

phoneNum_Regex_object = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
textToSearch = "Cell = 415-456-7896 and Mobile = 567-674-2398"
matched_obj = phoneNum_Regex_object.search(textToSearch)
print(matched_obj.group())

print(phoneNum_Regex_object.findall(textToSearch))


xmasRegex = re.compile(r'\d+\s\w+')
print(xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge'))