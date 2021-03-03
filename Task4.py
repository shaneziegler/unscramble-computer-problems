"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

# Create list of all numbers making outgoing calls - calls[0]
# Remove any from list that send texts - texts[0]
# Remove any from list that recieve texts - texts[1]
# Remove any from list that recieve calls - calls[1]
# Remove duplicates
# Sort list
telemarketers = []

for call in calls: # Create list of all numbers that make outgoing calls
    telemarketers.append(call[0].strip())

telemarketers = list(set(telemarketers)) # Remove dups

for text in texts: # Remove any numbers that send/receive texts
    if text[0].strip() in telemarketers:
        telemarketers.remove(text[0].strip())
    if text[1].strip() in telemarketers:
        telemarketers.remove(text[1].strip())

for call in calls: # Remove any numbers that received calls
    if call[1].strip() in telemarketers:
        telemarketers.remove(call[1].strip())

telemarketers.sort()
print("These numbers could be telemarketers:")
for telemarketer in telemarketers:
    print(telemarketer)