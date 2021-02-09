"""
By Kami Bigdely
Rename Method
Reference: https://parade.com/1039985/marynliles/pick-up-lines/
"""

def calc_area_under_grapg(graph):
    """Calculate the area under the input graph."""
    # bla bla bla.
    pass

#####################

def get_largest_value(li):
    """Returns the largest value in the given list"""
    m = li[0]
    for value in li:
        if value > m:
            m = value
    return m


li = [5, -1, 43, 32, 87, -100]
print(get_largest_value(li))

############################
def extract_words(sentence):
    """Extracts the words from a given sentence and returns them in an array"""
    words = sentence[0:].split(' ')
    return words

print(extract_words('If you were a vegetable, you’d be a ‘cute-cumber.'))
