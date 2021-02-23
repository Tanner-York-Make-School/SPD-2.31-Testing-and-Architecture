"""
By Kami Bigdely
Refactored by Tanner York
Move Field
"""

class Car:
    def __init__(self, engine, wheels, cabin, fuel_tank):
        self.engine = engine
        self.wheels = wheels
        # Set wheels' car reference into each wheel.
        for w in wheels:
            w.set_car(self)
            
        self.cabin = cabin
        self.fuel_tank = fuel_tank

    
class Wheel:
    def __init__(self, car = None, tpms=None, wheel_location = None):
        self.car = car
        self.wheel_location = wheel_location
        self.tpms = tpms

    def install_tire(self):
        print('remove old tube.')
        print('cleaned tpms: ', self.tpms.get_serial_number(), '.')
        print('installed new tube.')

    def read_tire_pressure(self):
        return self.tpms.get_pressure()

    def set_car(self, car):
        self.car = car


class Tpms:
    """Tire Pressure Monitoring System."""
    def __init__(self, serial_number):
        self.serial_number = serial_number
        self.sensor_transmit_range = 300 # [feet]
        self.sensor_pressure_range = (8,300) # [PSI]
        self.battery_life = 6 # [year]
        
    def get_pressure(self):
        return 3
    
    def get_serial_number(self):
        return self.serial_number
    
class Engine:
    def __init__(self):
        pass
    
class FuelTank:
    def __init__(self):
        pass
    
class Cabin:
    def __init__(self):
        pass    
    

if __name__ == '__main__':
    engine = Engine()
    wheels = [Wheel(None, Tpms(983408543), 'front-right'), Wheel(None, Tpms(4343083), 'front-left'), 
            Wheel(None, Tpms(23654835), 'back-right'), Wheel(None, Tpms(3498857), 'back-left')]

    cabin  = Cabin()

    tpms_di = {'front-right': Tpms(983408543), 'front-left':Tpms(4343083),
                'back-right':Tpms(23654835), 'back_left':Tpms(3498857)}

    fuel_tank = FuelTank()

    my_car = Car(engine, wheels, cabin, fuel_tank)


