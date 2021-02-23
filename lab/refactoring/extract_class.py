"""
By Kami Bigdely
Refactored by Tanner York
Extract Class
"""

foods = {'butternut squash soup':[45, True, 'soup','North African',\
     ['butter squash','onion','carrot', 'garlic','butter','black pepper', 'cinnamon','coconut milk']\
        ,'1. Grill the butter squash, onion, carrot and garlic in the oven until'
          'they get soft and golden on top 2. Put all in blender with'
          'butter and coconut milk. Blend them till they become puree. Then move the content into a pot'
               '. Add coconut milk. Simmer for 5 mintues.'],
        'shirazi salad':[5, True, 'salad','Iranian', ['cucumber', 'tomato', 'onion', 'lemon juice'], \
            '1. dice cucumbers, tomatoes and onions 2. put all into a bowl 3. pour lemon juice 3. add salt'
                '4. Mixed them thoroughly'],
        'Home-made Beef Sausage': [60, False, 'deli','All',['sausage casing', 'regular ground beef','garlic',\
            'corriander seeds','black pepper seeds','fennel seed','paprika'],'1. In a blender,'
                ' blend corriander seeds, black pepper seeds, fennel seeds and garlic to make'
                'the seasonings 2. In a bowl, mix ground beef with the'
                'seasoning 3. Add all the content to a sausage stuffer. Put the casing on'
                "the stuffer funnel. Rotate the stuffer's handle (or turn it on) to make your yummy sausages!"]}

class Recipe():
    """Class for representing recipes and how tho make them"""
    def __init__(self, name, prep_time, is_veggie, food_type, cuisine, ingredients, directions):
        """
        Creates a new Recipe object from the following info:
            name (string): name of the recipe
            ingredients (Array(string)): a list of the recepies ingredients 
            prep_time (int): minutes it take to make recipe
            cuisine (string): where the recipe origonated
            is_veggie (bool): wether the recipe is veggie based
            info (Array(any)): list of general info like cook time
            directions(string): the directions for the recipe
        """
        self.name = name
        self.ingredients = ingredients
        self.prep_time = prep_time
        self.is_veggie = is_veggie
        self.type = food_type 
        self.cuisine = cuisine
        self.directions = directions

    def describe(self):
        print("Name:", self.name)
        print("Prep time:", self.prep_time, "mins")
        print("Is Veggie?", 'Yes' if self.is_veggie else "No")
        print("Food Type:", self.type)
        print("Cuisine:", self.cuisine)
        for item in self.ingredients:
            print(item, end=', ')
        print()
        print("recipe", self.directions)
        print("***")


if __name__ == '__main__':
    for key, value in foods.items():
        recipe = Recipe(key, value[0], value[1], value[2], value[3], value[4], value[5])
        recipe.describe()
