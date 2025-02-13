"""
By Kami Bigdely
Remove assignment to method parameter.
"""

class Distance:
    """Creates a new distance object with the given a value and unit"""
    def __init__(self, value, unit):
        self.unit = unit
        self.value = value

class Mass:
    """Creates a new Mass object with the given value and unit"""
    def __init__(self, value, unit):
        self.value = value
        self.unit = unit

def calculate_kinetic_energy(mass, distance, time):
    """Calculates and returns the kenetic energy of the given mass, distance, and time"""
    if distance.unit != 'km':
        if distance.unit == "ly": # [ly] stands for light-year (measure of distance in astronomy)
            # convert from light-year to km unit
            in_km = distance.value * 9.461e12
            distance_km = Distance(in_km, "km") 
        else:
            print ("unit is Unknown")
            return

    speed = distance_km.value/time # [km per sec]
    if mass.unit != 'kg':
        if mass.unit == "solar-mass":
            # convert from solar mass to kg
            value = mass.value * 1.98892e30 # [kg]
            mass_kg = Mass(value, 'kg')
        else:
            print ("unit is Unknown")
            return

    kinetic_energy = 0.5 * mass_kg.value * speed ** 2
    return kinetic_energy

if __name__ == '__main__':
    mass = Mass(2, "solar-mass")
    distance = Distance(2, 'ly')
    print(calculate_kinetic_energy(mass, distance, 3600e20))