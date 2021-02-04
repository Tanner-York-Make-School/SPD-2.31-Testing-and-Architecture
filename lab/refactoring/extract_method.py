"""
Written by Kamran Bigdely
Example for Compose Methods: Extract Method.
"""
import math

def grades_input(n_student):
    """Gets grade inputs from the user."""
    grade_list = []
    for _ in range(0, n_student):
        grade_list.append(int(input('Enter a number: ')))
    return grade_list

def calc_mean(values):
    """Calculates the mean of a list of numbers."""
    values_sum = 0
    for value in values:
        values_sum += value
    return values_sum / len(values)

def calc_standard_deviation(values, mean):
    """Calculates the standard deviation of a given list of numbers and its mean"""
    sum_of_sqrs = 0
    for value in values:
        sum_of_sqrs += (value - mean) ** 2
    return math.sqrt(sum_of_sqrs / len(values))

def print_stat():
    """Prints out the mean and standard deviation of a user inputed list of grades."""
    # Get the inputs from the user
    grade_list = grades_input(5)
    # Calculate the mean and standard deviation of the grades
    mean = calc_mean(grade_list)
    std = calc_standard_deviation(grade_list, mean)
    # print out the mean and standard deviation in a nice format.
    print('****** Grade Statistics ******')
    print("The grades's mean is:", mean)
    print('The population standard deviation of grades is: ', round(std, 3))
    print('****** END ******')

print_stat()
