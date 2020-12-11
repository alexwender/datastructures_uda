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

phone_numbers = set()
for item in texts:
    phone_numbers.add(item[0])
    phone_numbers.add(item[1])

for item in calls:
    phone_numbers.add(item[0])
    phone_numbers.add(item[1])

print(f"There are {len(phone_numbers)} different telephone numbers in the records")
