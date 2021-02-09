"""
By Kami Bigdely
Split temp variable
"""

def save_into_db(info):
    """Saves the given infromation to the database"""
    print(f"{info} was saved into the databse")

if __name__ == '__main__':
    username = input('Please enter your username: ')
    save_into_db(username)
    birth_year = int(input('Please enter your birth year: '))
    age = 2020 - birth_year
    print("You are",age, "years old.")
