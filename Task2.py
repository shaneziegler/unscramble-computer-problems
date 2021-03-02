"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

call_time = {} # Create a blank dictionary to add up our call times in
for call in calls:
    if call[0] in call_time:
        call_time[call[0]] += int(call[3]) # Add call seconds to time
    else:
        call_time[call[0]] = int(call[3]) # Not in dictionary yet
    if call[1] in call_time:
        call_time[call[1]] += int(call[3]) # Add call seconds to time
    else:
        call_time[call[1]] = int(call[3]) # Not in dictionary yet

# Find longest call time in our dictionary
longest = 0
longest_phonenum = ""
for key, value in call_time.items():
    if value > longest: # Save longest call time and phone number
        longest = value
        longest_phonenum = key

print(f"{longest_phonenum} spent the longest time, {longest} seconds, on the phone during September 2016.")
