"""
Exercise 3
"""

# PART 1: Gather Information
#
# - What error message (if any) is there?
# Traceback (most recent call last):
#   File "exercise-3.py", line 34, in <module>
#     answer = insertion_sort([5, 2, 3, 1, 6])
#   File "exercise-3.py", line 26, in insertion_sort
#     while key < arr[j] : 
# IndexError: list index out of range
#
# - What line number is causing the error?
# Line 26
#
# - What can you deduce about the cause of the error?
#  There's an issue with j reaching a negative number before the while loops stops


# PART 2: State Assumptions
#
# The first thing that we should be doing is setting the key to 2 and j to the 
# index of 5. We add a print statment to see if this is happening... It is, so
# this is not necessarily where the issue is
#
# Next, if the value before the key value is larger, we move it up until we
# find a value that is smaller or j reaches 0. We can add a print statment in
# the while loop to see if this is happening... It's not, j goes bellow 0 and
# continues swapping values. This may not be where the error is exactly but 
# this is a major bug that could eventaully cause the error we're getting. 
#
# Next, to solve this bug we can add another condition to the while loop,
# stopping it once it goes bellow zero. Running the code agian for testing we
# find that the list is sorted without error.

def insertion_sort(arr):
    """Performs an Insertion Sort on the array arr."""
    for i in range(1, len(arr)):
        key = arr[i] 
        j = i-1
        while key < arr[j] and j >= 0:
            arr[j+1] = arr[j] 
            j -= 1
        arr[j+1] = key
    return arr

if __name__ == '__main__':
    print('### Problem 3 ###')
    answer = insertion_sort([5, 2, 3, 1, 6])
    print(answer)

