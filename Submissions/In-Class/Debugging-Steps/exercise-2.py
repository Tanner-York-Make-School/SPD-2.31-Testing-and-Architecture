"""
Exercise 2
"""

# PART 1: Gather Information
#
# Gather information about the source of the error and paste your findings here. E.g.:
# - What is the expected vs. the actual output?
# We are getting False, False as an output when we should be getting False, True
#
# - What error message (if any) is there?
# There is no error message
#
# - What line number is causing the error?
# Through Stating assumption below,  I've found the issue on line 31 and 32
#
# - What can you deduce about the cause of the error?
# I can deduce that the cause of the error is that the algorithm is not checking
# the entire list for consecutive numbers but only the first three


# PART 2: State Assumptions
#
# The first thing we do is that we can assume that the test that is meant to be true
# but is false, is where the bud is comming from
#
# Next, the loop for going through indexes should be looping through the entire
# list untill a 3 consecutivenumber pattern is found or it reaches the second to 
# last index. We can test is this is working by addding a print statment. It is only 
# reaching the first index so we can assume the issue is being raised here.
#
# Next, we check if the if statement is returning the proper value for the first index.
# By adding a print statement we can find that is is properly returning false. However,
# we also see that the else statment is returing false, thus ending the function eartly
# when is should continue the itteration. We've found the bug.
#
# Finally, we fix the error by removing the else statment and test if it's working by
# running the code again. It's returning the expected False, True so we can conclude
# that the bug is fixed for the given test cases.

def contains_3_consecutive(list_of_nums):
    """Return True if the list contains 3 consecutive numbers each increasing by 1."""
    for i in range(len(list_of_nums) - 2):
        if (list_of_nums[i+1] == list_of_nums[i] + 1 and
            list_of_nums[i+2] == list_of_nums[i] + 2):
            return True
    return False

if __name__ == '__main__':
    print('### Problem 2 ###')
    answer1 = contains_3_consecutive([1, 2, 4])
    print(answer1) # should print False

    answer2 = contains_3_consecutive([4, 1, 2, 3])
    print(answer2) # should print True