"""
By Kami Bigdely
Decompose conditional: You have a complicated conditional(if-then-else) statement. Extract
methods from the condition, then part, and else part(s).
"""

def make_alert_sound():
    print('made alert sound.')

def make_accept_sound():
    print('made acceptance sound')

def contains_toxin(ingredients):
    toxins = ['sodium nitrate', 'sodium benzoate', 'sodium oxide']
    return any(ingredient in toxins for ingredient in ingredients)

ingredients = ['sodium benzoate']
if contains_toxin(ingredients):
    print('!!!')
    print('there is a toxin in the food!')    
    print('!!!')
    make_alert_sound()
else:
    print('***')
    print('Toxin Free')
    print('***')
    make_accept_sound()
