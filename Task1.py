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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
list = []
for text in texts:
    list.append(text[0])
    list.append(text[1])
count = len(list)
for call in calls:
    list.append(call[0])
    list.append(call[1])
count = len(list)

phone_numbers_set = set(list)
count = len(phone_numbers_set)

print(f"There are {len(phone_numbers_set)} different telephone numbers in the records.")
