"""
Adapted from a Java code in the "Refactoring" book by Martin Fowler.
Replace temp with query
Code snippet. Not runnable.
"""

def get_price(quantity, item_price):
    """Gets the total price of a purchace given the quantiy and the items price"""
    base_price = quantity * item_price
    discount_factor = get_discount_factor(base_price)
    return base_price * discount_factor

def get_discount_factor(base_price):
    """Gets the discount facort for a given base price"""
    return 0.95 if base_price > 1000 else 0.98
    
