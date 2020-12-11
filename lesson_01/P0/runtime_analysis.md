# Runtime Analysis

# Task 0

The runtime is is O(1) meaning that it has a constant runtime independent of the number of elements present in the data

# Task 1
The data has to be looped through once for each data set. With n being the number of elements in texts and m being the number of elements in calls we have O(n + m) = O(k)

# Task 2
The algorithm has to loop once through all the calls so with m being the number of entries in calls, we start with O(m).
The small loop within the calls loop has a constant runtime as only 2 elements are looped through and can therefore be ignored.
The second loop has to go through all the recorded phone times. In a worst case scenario, each call was between two different phone numbers. That would mean that this dictionary would have 2m entries. The runtime would be then O(m + 2*m) = O(3m) = O(m), meaning still linear runtime.

# Task 3
## Part A
For the analysis of Part A, the algorithm we start with a loop through all the phone calls, thus having a runtime of O(m). After that the time complexity for creating a set out of the list is to be considered. Looking at the python wiki for time complexity (https://wiki.python.org/moin/TimeComplexity), there is a worst case scenario for creating the set. Basically, the every entry has to be checked against being already included in the set. As the set is implemented as a hash "map", this is on normally done with O(1) complexity, meaning total O(m) complexity. However, there is a worst case scenario, where the function of the hash value would produce a lot of collisions, increasing the lookup runtime of the set to be O(n) and thus having a total of O(m^2) runtime.
The sorting of the set is done with the timsort algorithm implemented in python, having a complixity of O(log m * m)
So for part A we have to answers:
average complexity: O(2m + log m * m) = O(log m * m)
worst case (hash collisions): O(m + m^2 + log m * m) = O(m^2)

## Part B
The complexity of Part B starts from creating the list of phone calls from Part A, i.e. O(m). This list has to be parsed again while checking if the new entry 
is also a bangalore number, meaning another O(m). So in total O(2m) = O(m)

## Side Note
Part A could have been done without creating a list of entries and instead updating a set directly. But with the knowledge of Part B, the implementation with creating a complete list is used because it is necessary for Part B

# Task 4
At first all entries in the calls list have to be parsed and all receiving numbers have to be put into a set. Like in Task 3, this takes on overage O(m) runtime and in a worst case scenario (hash collisions) O(m^2). 
After all calls have been parsed, all text sending and receiving numbers have to be put also into the set, leading to O(n+2m) = O(max(n,m))=O(k) on average or O(n^2 + 2m^2) = O((max(n,m))^2) = O(k^2) complexity.
After all this "non_telemarkter" numbers are clear, the calling numbers of the calls list have to be checked against these. Unlike in the previous loop, there are two checks for entries in a set here, resulting in a runtime of O(m) on average or O(m^3) for the worst case scenario.
In the last step the python timsort algorithm is again used for the output which takes O(log l * l) complexity with l being the number of found telemarketer candidates.
In total the runtime for all parts are
on average: O(k + m + log l * l) = O(log m * m)
worst case: O(k^2 + m^3 + log l * l) = O(m^3)