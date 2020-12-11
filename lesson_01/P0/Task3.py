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


def is_bangalore_number(input_number, is_only_prefix=False):
  """Checking for a number from bangalore, i.e. a valid number with a (080)
  prefix. If is_only_prefix is set, then only the prefix will be checked.

  Args:
      input_number (str): Input number as a string
      is_only_prefix (bool, optional): Checking only the prefix. Defaults to False.

  Returns:
      [type]: [description]
  """
  
  # using the regex module of python
  # import in this position is not a very good idea normally, 
  # but I used it here for better an easier review
  import re
  regex_string = "\(080\)"
  if not is_only_prefix:
    regex_string += "[0-9]+"
  found_match = re.match(regex_string, input_number)
  if found_match:
    return True
  else:
    return False

def extract_area_code_or_mobile_prefix(input_number):
  """Extraction of the area code or mobile prefix of a given number (as string).
  Area code is defined as the number enclosed by parenthesis and the mobile prefix
  is given by the first four digits if the number starts with a 7, 8 or 9 and contains
  a whitespace character

  Args:
      input_number (str]: input number as string

  Returns:
      str: extracted area or mobile prefix, None with neither is present
  """
  import re
  # the used regex only searches for area code (parenthesis) or mobile prefix
  # (first 4 digits, whitespace and trailing numbers) because
  # the telemarketer numbers are already excluded by this two criteria
  found_match = re.match(
    r"(?P<area_code>\(0[0-9]+\))|(?P<mobile_prefix>[7,8,9][0-9]{3})(?P<rest_pre_whitespace>[0-9]*)\s(?P<post_whitespace>[0-9]+)",
    input_number)
  if found_match:
    group_dict = found_match.groupdict()
    if group_dict.get("area_code", None):
      return group_dict["area_code"]
    elif group_dict.get("mobile_prefix", None):
      # test if whitespace is in the "middle"
      pre_whitespace_length = len(group_dict.get("rest_pre_whitespace", 0)) + len(group_dict.get("mobile_prefix"))
      post_whitespace_length = len(group_dict.get("post_whitespace", 0))
      if pre_whitespace_length == post_whitespace_length:
        return group_dict["mobile_prefix"].rstrip()
      else:
        return None
  else:
    return None

# Here I create a list although a set would be sufficient for the Part A
# task. But for Part B the whole list is needed
called_by_bangalore = []
for phone_call in calls:
  if is_bangalore_number(phone_call[0]):
    extracted_number = extract_area_code_or_mobile_prefix(phone_call[1])
    if extracted_number:
      called_by_bangalore.append(extracted_number)
sorted_set_called_by_bangalore = sorted(set(called_by_bangalore))
print("The numbers called by people in Bangalore have codes:\n{}".format(
  "\n".join(sorted_set_called_by_bangalore)))

total_number_called = len(called_by_bangalore)
called_bangalore = 0
for called_number in called_by_bangalore:
  # Here, the is_only_prefix flag is used because only prefixes are available.
  if is_bangalore_number(called_number, is_only_prefix=True):
    called_bangalore += 1

percentage_bangalore = float(called_bangalore) / total_number_called * 100.
print("{:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(
  percentage_bangalore
))