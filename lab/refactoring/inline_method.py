"""
By Kami Bigdely
Inline method.
Refactor this program to improve its readability.
"""

LEGAL_DRINKING_AGE = 21
class Person:
    """Person class for creating Person objects from a given age"""
    def __init__(self, my_age):
        """Creates a new Person object"""
        self.age = my_age

    def enter_night_club(self):
        """Checks the enterance avalability for the Person"""
        if self.age > LEGAL_DRINKING_AGE:
            print("Allowed to enter.")
        else:
            print("Enterance of minors is denited.")

person = Person(17.9)
person.enter_night_club()
        