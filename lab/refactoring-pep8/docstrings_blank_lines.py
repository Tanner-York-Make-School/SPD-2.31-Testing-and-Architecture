# by Kami Bigdely
# Docstrings and blank lines
class OnBoardTemperatureSensor:
    VOLTAGE_TO_TEMP_FACTOR = 5.6
    
    def __init__(self):
        """Creates a new OnboardTemperatreSensor object with a voltage factor of 5.6"""
        pass

    def read_voltage(self): 
        """Reads and returns the sensors current voltage"""       
        return 2.7

    def get_temperature(self):
        """Calculates and returns the temperature based on the voltage and voltage temp factor"""
        return self.read_voltage() * OnBoardTemperatureSensor.VOLTAGE_TO_TEMP_FACTOR # [celcius]
  
class CarbonMonoxideSensor:
    VOLTAGE_TO_CO_FACTOR = 0.048

    def __init__(self, temperature_sensor):
        """
        Creates a new CarbonMonoxideSensorObject.
            Args:
                temerature_sensor(OnBoardTemperatureSensor): a sensor for getting the on board temerature
            Returns:
                CarbonMonoxideSensor: a new CarbonMonoxideSensor object
        """
        self.on_board_temp_sensor = temperature_sensor
        if not self.on_board_temp_sensor:
            self.on_board_temp_sensor = OnBoardTemperatureSensor()

    def get_carbon_monoxide_level(self):
        """Get and returns the current carbon monoxide level"""
        sensor_voltage = self.read_sensor_voltage()
        self.carbon_monoxide = self.convert_voltage_to_carbon_monoxide_level(
            sensor_voltage, self.on_board_temp_sensor.get_temperature())
        return self.carbon_monoxide

    def read_sensor_voltage(self):
        """Reads and returns the sensors current voltage"""
        # In real life, it should read from hardware.        
        return 2.3

    def convert_voltage_to_carbon_monoxide_level(self, voltage, temperature):
        """
        Converts and returns the voltage to carbon monoxide levels
            Args:
                voltage(double): a double repesentation of voltage
                temperature(double): a double representation of temeratore in celcius
            Returns:
                voltage-to-cm level(double): double representation of the voltage to
                    carbom monoxide level calculation
        """
        return voltage * CarbonMonoxideSensor.VOLTAGE_TO_CO_FACTOR * temperature
    
class DisplayUnit:
    def __init__(self):
        """Creates a new DisplayUnit object for diplaying messages"""
        self.string = ''

    def display(self,msg):
        """Prints out the given msg"""
        print(msg)

class CarbonMonoxideDevice():
    def __init__(self, co_sensor, display_unit):
        """
        Creates a new CarbonMonoxideDevice object for displaying carbon monoxide levels.
            Args:
                co_sensor(CarbonMonoxideSensor): sensor for read carbon monoxide levels
                display_unit(DisplayUnit): unit used to display messages
            Returns:
                CarbonMonoxideDevice: a new CarbonMonoxideDevice object
        """
        self.carbonMonoxideSensor = co_sensor 
        self.display_unit = display_unit   

    def Display(self):
        """Prints the current carbon monoxide level"""
        msg = 'Carbon Monoxide Level is: ' +  str(self.carbonMonoxideSensor.get_carbon_monoxide_level())
        self.display_unit.display(msg)

if __name__ == "__main__":
    temp_sensor = OnBoardTemperatureSensor()
    co_sensor = CarbonMonoxideSensor(temp_sensor)
    display_unit = DisplayUnit()
    co_device = CarbonMonoxideDevice(co_sensor, display_unit)
    co_device.Display()
    