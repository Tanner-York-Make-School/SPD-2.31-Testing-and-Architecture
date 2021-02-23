"""
By Kamran Bigdely
Refactored by Tanner York
Extract superclass
"""

class Enemy():
    """Class representation of an enemy"""
    def __init__(self):
        """Creates a new enemy object with health set to 100"""
        self.health = 100

    def take_damage(self, damage):
        """Reduces the enemys health by the given damage"""
        self.health -= damage

class AngryMushroom(Enemy):
    """Class representation of an Angry Mushroom"""
    def __init__(self):
        """Creates a new AngryMushroom object with the Enemy class"""
        super().__init__()

    def spread_poison(self):
        """Spreads poison around itself"""
        print('spreading poison!')


class AngryBot(Enemy):
    """Class representation of an Angry Bot"""
    def __init__(self):
        """
        Creates a new AngryBot object with the Enemy class and it's
        Emeny super class intialized with 40 bulets
        """
        super().__init__()
        self.n_bullets = 40

    def punch_iron_fist(self):
        """Puches with its fist"""
        print("punching with iron fist!")

    def shoot(self):
        """Shoots it's gun"""
        print("shot a bullet!")
        self.n_bullets -= 1


class AgressiveAlligator(Enemy):
    """Class representation of an Agressive Alligator"""
    def __init__(self):
        """Creates new AgressiveAlligator with it's Enemy super class"""
        super().__init__()

    def bite(self):
        """Bites"""
        print('bitting!')


if __name__ == '__main__':
    angryMushroom = AngryMushroom()
    print("initial health level:", angryMushroom.health)
    angryMushroom.take_damage(25)
    print("took damage!")
    print("current health level:",angryMushroom.health)
