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

# save duration in dictionary, very efficient for checking if value is present
# and adding a key
phone_time = {}
for item in calls:
    duration = int(item[3])

    for phone_number in (item[0], item[1]):
        phone_time[phone_number] = phone_time.get(phone_number, 0) + duration

longest_duration = 0
longest_duration_number = None

# sorting is not necessary, just going through over all items once
for phone_number, duration in phone_time.items():
    if duration > longest_duration:
        longest_duration = duration
        longest_duration_number = phone_number

print(f"{longest_duration_number} spent the longest time, {longest_duration} seconds, on the phone during September 2016.")