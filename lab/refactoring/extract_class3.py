"""
By Kami Bigdely
Refactored by Tanner York
Extract class
"""

WELL_DONE = 3000
MEDIUM = 2500
COOKED_CONSTANT = 0.05

class Food():
    def __init__(self, well_done, medium, cooked_constant):
        self.well_done = well_done
        self.medium = medium
        self.cooked_constant = cooked_constant

    def is_cookeding_criteria_satisfied(self, time, temperature, 
                                        pressure, desired_state):
        return self.is_well_done(time, temperature, pressure, desired_state) or \
            self.is_medium(time, temperature, pressure, desired_state)

    def is_well_done(self, time, temperature, pressure, desired_state):    
        return desired_state == 'well-done' and  \
            self.get_cooking_progress(time, temperature, pressure) >= self.well_done

    def is_medium(self, time, temperature, pressure, desired_state):
        return desired_state == 'medium' and  \
            self.get_cooking_progress(time, temperature, pressure) >= self.medium

    def get_cooking_progress(self, time, temperature, pressure):
        return time * temperature * pressure * self.cooked_constant


if __name__ == '__main__':
    time = 30 # [min]
    temp = 103 # [celcius]
    pressure = 20 # [psi]
    desired_state = 'well-done'

    food_to_be_cooked = Food(3000, 2500, 0.05)

    if food_to_be_cooked.is_cookeding_criteria_satisfied(time, temp, pressure, desired_state):
        print('cooking is done.')
    else:
        print('ongoing cooking.')