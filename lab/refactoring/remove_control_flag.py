"""
By Kami Bigdely
Remove control flag
"""

def find_food(food, fridge):
    for item in fridge:
        if food in item:
            item_name = item
            break
    return item_name

if __name__ == "__main__":
    food = 'wesabi'
    food_list = ['onion', 'cucumber','Guacamole', 'kabob barg', 'wesabi']
    found_item = find_food(food, food_list)
    print(food, "Found: " + found_item  if found_item != None else "not found")
