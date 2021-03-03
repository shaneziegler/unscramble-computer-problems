"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

def get_prefix(str):
    str = str.strip()
    pre = ""
    if str[0] == "(": # Do fixed line prefix
        end = str.find(")")
        if end == -1:
            return None
        else:
            pre = str[1:end]
    elif str[0:2] == "140": # Do telemarketer prefix
        pre = "140"
    elif str.find(" ") != -1: # Do mobile prefix
        pre = str[0:str.find(" ")]
    else: # Unknown Format
        return None
    return pre

code_list = []

for call in calls:
    prefix1 = get_prefix(call[0])
    prefix2 = get_prefix(call[1])
    if prefix1 == '080':
        code_list.append(prefix2)



print("The numbers called by people in Bangalore have codes:")
code_list = list(set(code_list))
code_list.sort()
for code in code_list:
    print(code)

