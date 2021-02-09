"""
By Kami Bigdely
Split temporary variable
"""

PATTY = 70 # [gr]
PICKLE = 20 # [gr]
TOMATOES = 25 # [gr]
LETTUCE = 15 # [gr]
BUNS = 95 # [gr]
NY_BURGER_WEIGHT = (2 * PATTY + 4 * PICKLE + 3 * TOMATOES + 2 * LETTUCE
                + 2 * BUNS)
print("NY Burger Weight", NY_BURGER_WEIGHT)

KIMICHI = 30 # [gr]
MAYO = 5 # [gr]
GOLDEN_FRIED_ONION = 20 # [gr]
SEOL_BURGER_WEIGHT = (2 * PATTY + 4 * PICKLE + 3 * TOMATOES
                + KIMICHI + MAYO + GOLDEN_FRIED_ONION + 2 * BUNS)
print("Seoul Kimchi Burger Weight", SEOL_BURGER_WEIGHT)
