"""
Written by Kamran Bigdely
Example for Compose Methods: Extract Method.
"""
import math

def calc_difference(x1, y1, x2, y2, is_circle):
    """Calculates the difference between two points or circles"""
    if is_circle:
        return math.sqrt((x1-x2)**2 + (y1 - y2)**2)
    return math.sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2))

xc1, yc1 = 4, 4.25
xc2, yc2 = 53, -5.35

# Calculate the distance between the two circle
distance = calc_difference(xc1, yc1, xc2, yc2, True)
print('distance', distance)

# *** somewhere else in your program ***

xa, ya = -36, 97
xb, yb = .34, .91
# calcualte the length of vector AB vector which is a vector between A and B points.
length = calc_difference(xa, ya, xb, yb, False)
print('length', length)
