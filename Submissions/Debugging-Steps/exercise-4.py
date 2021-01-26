"""
Exercise 4
"""

# PART 1: Gather Information
#
# - What is the expected vs. the actual output?
# We're supposed to get the index of 7 but we're acctaully getting an error
#
# - What error message (if any) is there?
# Traceback (most recent call last):
#   File "exercise-4.py", line 50, in <module>
#     answer = binary_search([1, 2, 4, 5, 7], 7)
#   File "exercise-4.py", line 46, in binary_search
#     return binary_search(arr, element, mid, high)
#   File "exercise-4.py", line 46, in binary_search
#     return binary_search(arr, element, mid, high)
#   File "exercise-4.py", line 46, in binary_search
#     return binary_search(arr, element, mid, high)
#   [Previous line repeated 995 more times]
#   File "exercise-4.py", line 31, in binary_search
#     if high == None:
# RecursionError: maximum recursion depth exceeded in comparison
#                    ^
# 
# - What line number is causing the error?
# Line 31
#
# - What can you deduce about the cause of the error?
# Because there is a recursion error we can assum that the error 
# has something to do with the recusive function not stopping


# PART 2: State Assumptions
# 
# The first thing we do is set high to the last index in the list
# to start off the search. Let's add a print statment to see if this
# is happening... Yes, high is properly getting set to 4 (the last index)
#
# Next, we need to make sure that the high index is not less than the
# low index. We know this isn't happening at some point because we
# would't get a recusion error if it was. However, this is not 
# necessarully where the bug is.
#
# Next, we set the mid varible to the middle of the array (high and low).
# Lets add a print statment and break to see if this is happening... Yep,
# the midpoint is 2.
#
# Next we check if the value at mid is equal to the value we're looking for
# and because the first value is 4 and we're looking for 7 it should return
# False. Adding a print statmen shows that is indeed returns False
# 
# Next we determin if the value is larger or smaller than the mid an if we
# need to recusivley search on the high or low side. Lets add a print 
# statment to see if this is happening... Yep, it's verifying that the mid
# is lower than the high.
#
# Next, we need to start the recursive search between the mid and high. We can't
# really add a print statment to test this one but now that we know that the other
# steps are working, we can metally or visually go through untill we find the issue.
# Once we do this, we get to a point where mid is stuck on 3 untill the recusion
# error is thrown. This is because we're not removing the mid value when we start
# the recusive search and thus we found our bug. 
#
# Finally, we can fix the bug by adding +1 to the mid in the high search and -1 
# to the mid in the low search. Running the code agian we find that we get the
# expected output of index 4

def binary_search(arr, element, low=0, high=None):
    """Returns the index of the given element within the array by performing a binary search."""
    if high == None:
        high = len(arr) - 1

    if high < low:
        return -1

    mid = (high + low) // 2

    if arr[mid] == element: 
        return mid

    elif arr[mid] > element:
        return binary_search(arr, element, low, mid-1)

    else: 
        return binary_search(arr, element, mid+1, high)


if __name__ == '__main__':
    answer = binary_search([1, 2, 4, 5, 7], 7)
    print(answer)