"""
By Kami Bigdely
Refactored by Tanner York
Extract class
"""

first_names = ['elizabeth', 'Jim']
last_names = ['debicki', 'Carrey']
birth_year = [1990, 1962]
movies = [['Tenet', 'Vita & Virgina', 'Guardians of the Galexy', 'The Great Gatsby'],\
     ['Ace Ventura', 'The Mask', 'Dubm and Dumber', 'The Truman Show', 'Yes Man']]
emails = ['deb@makeschool.com', 'jim@makeschool.com']

class Actor():
    """Class for representing actors"""
    def __init__(self, first_name, last_name, birth_year, movies, email):
        """
        Creates a new Actor object with the following info:
            first_name(string): the actors first name
            last_name(string): the actors last name
            birth_year(int): year the actor was born (YYYY)
            moies(List(string)): list of movies the actors been in
            email(string): actors email address
        """
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year
        self.movies = movies
        self.email = email

def send_hiring_email(email):
    print("email sent to: ", email)
    
for i, value in enumerate(emails):
    actor = Actor(first_names[i], last_names[i], birth_year[i], movies[i], emails[i])
    print(actor.birth_year)
    if actor.birth_year > 1985:
        print(actor.first_name, actor.last_name)
        print('Movies Played: ', end='')
        for m in actor.movies:
            print(m, end=', ')
        print()
        send_hiring_email(actor.email)
