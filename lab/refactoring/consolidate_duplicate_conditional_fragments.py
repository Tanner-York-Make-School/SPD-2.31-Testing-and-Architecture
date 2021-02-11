"""
By Kami Bigdely
Consolidate duplicate conditional fragments
"""

def add(mix, something):
    mix.append(something)
    return mix

def mix_ice_with_cream():
    print('mixed ice with cream.')
    return ['ice', 'cream']

def is_coffee(drink):
    return 'coffe' in drink

def is_strawberry_milkshake(drink):
    return 'strawberry milkshake' in drink

def make_drink(drink, addons):
    mix = []

    if is_coffee(drink):
        mix = add(mix, 'coffee')
    elif is_strawberry_milkshake(drink):
        mix = mix_ice_with_cream()
        mix = add(mix, 'strawberry')
    
    mix = add(mix, addons)
    return mix

final_drink = make_drink('strawberry milkshake', ['milk','sugar'])
print(final_drink)
