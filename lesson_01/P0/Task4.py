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

non_telemarketers_set = set()
non_telemarketers_set.update(
    [number[1] for number in calls]
)
for text_info in texts:
    non_telemarketers_set.update(
        [
            text_info[0],
            text_info[1],
        ]
    )

telemarketer_candidates = set()
for number_info in calls:
    if number_info[0] not in non_telemarketers_set:
        telemarketer_candidates.add(number_info[0])
telemarketer_candidates = sorted(telemarketer_candidates)
print("These numbers could be telemarketers:\n{}".format(
    "\n".join(telemarketer_candidates)))
