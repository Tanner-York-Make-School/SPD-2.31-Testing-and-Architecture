"""
Exercise 1
"""

# PART 1: Gather Information
#
# - What is the expected vs. the actual output?
# We expect to get 4 but are getting an error instead
#
# - What error message (if any) is there?
# Traceback (most recent call last):
#   File "exercise-1.py", line 31, in <module>
#     answer = find_largest_diff([5, 3, 1, 2, 6, 4])
#   File "exercise-1.py", line 23, in find_largest_diff
#     diff = abs(list_of_nums[i] - list_of_nums[i+1])
# IndexError: list index out of range
#
# - What line number is causing the error?
# Line 31
#
# - What can you deduce about the cause of the error?
# One of the results of substracting the two of the numbers is too large for the array size


# PART 2: State Assumptions
#
#  The first thing we do is set largest_diff to 0 and we know this is working.
#  Next, we loop over each index in the list and set its value into i. Let's see if that's
#  happening by addinf a print statement for the variable i... Yes and No, it is printing 
#  out 0-4 smoothly but then the error is being through on index 5.
#  
#  Next, sinse we know the issue is on line 39 and it's happening on the last index (5),
#  we can infer that it's an issue with the indexing. Now, if we look at the indexing for
#  the last list_of_nums in the equasion, we can see that a 1 is being added to every
#  index and because 5 + 1 is 6 and the largest index we can go to is 5 we know that this
#  is were are error is.
#  
#  Next, we can think of a solustion to this issue. In this case because the +1 is
#  required we need to do something about the indexes we are interating through and that
#  can be solved by adding a -1 to the len(list_of_nums) so it only goes to 4.
#
#  Finaly, lets run the code and see if this fixed the code or if there is still a problem...
#  Nope, we get the expected 4 as on output so that mean there aren't any problems that we
#  can see with the given test right now.

def find_largest_diff(list_of_nums):
    """Find the largest difference between *consecutive* numbers in a list."""
    largest_diff = 0
    for i in range(len(list_of_nums)-1): # The issue was here and -1 was added to fit it
        diff = abs(list_of_nums[i] - list_of_nums[i+1])
        if diff > largest_diff:
            largest_diff = diff

    return largest_diff

if __name__ == '__main__':
    print('### Problem 1 ###')
    answer = find_largest_diff([5, 3, 1, 2, 6, 4])

    # This should print 4, as the largest diff between consecutive numbers is between 2 and 6
    print(answer)