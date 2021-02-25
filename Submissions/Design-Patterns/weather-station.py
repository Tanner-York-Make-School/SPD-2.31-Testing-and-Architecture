class Subject:
    """Class for representing a subject for observers to subscribe to"""
    def register_observer(self, observer):
        """Regisures an observer to the subject"""

    def remove_observer(self, observer):
        """Removes an observer from subscribing to the subject"""

    def notify_observers(self):
        """Notifys all subscribed observers that the subject has updated"""

# The observer class is implemented by all observers,
# so they all have to implemented the update() method. Here
# we're following Mary and Sue's lead and
# passing the measurements to the observers.
class Observer:
    """Class representation of an observer for staying up to date on a subject"""
    def update(self, temp, humidity, pressure):
        """Updates the value that the observer watches"""
        self.temperature = temp
        self.humidity = humidity
        self.pressure = pressure
        self.display()

    def display(self):
        """Displays the dispays observers information"""

# weather_data now implements the subject interface.
class WeatherData(Subject):
    """Class representation of the weather data subject"""
    def __init__(self):
        """Creates a new WeatherData object"""
        self.observers = []
        self.temperature = 0
        self.humidity = 0
        self.pressure = 0

    def register_observer(self, observer):
        """When an observer registers, we just
        add it to the end of the list."""
        self.observers.append(observer)

    def remove_observer(self, observer):
        """When an observer wants to un-register,
        we just take it off the list."""
        self.observers.remove(observer)

    def notify_observers(self):
        """We notify the observers when we get updated measurements
        from the Weather Station."""
        for ob in self.observers:
            ob.update(self.temperature, self.humidity, self.pressure)

    def measurements_changed(self):
        """Idicates that the observers need to me updated"""
        self.notify_observers()

    def set_measurements(self, temperature, humidity, pressure):
        """Sets the weather datas measurements to the given measurements"""
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure

        self.measurements_changed()


class CurrentConditionsDisplay(Observer):
    """Class representation of a current condition dispaly"""
    def __init__(self, weather_data):
        """Creates a new CurrentConditionsDispaly object"""
        self.temperature = 0
        self.humidity = 0
        self.pressure = 0

        self.weather_data = weather_data # save the ref in an attribute.
        weather_data.register_observer(self) # register the observer
                                           # so it gets data updates.

    def display(self):
        """Displays the current conditions"""
        print("Current conditions:", self.temperature,
              "F degrees and", self.humidity,"[%] humidity",
              "and pressure", self.pressure)
        print("========================")

# implement StatisticsDisplay class and ForecastDisplay class.
class StatisticsDisplay(Observer):
    """Class representation of a statistics display"""
    def __init__(self, weather_data):
        """Creats a new StatisitcDispaly object that observes
        the given weather data subject"""
        self.temperature = 0
        self.temperatures = []
        self.humidity = 0
        self.humidities = []
        self.pressure = 0
        self.pressures = []

        self.weather_data = weather_data
        weather_data.register_observer(self)

    def update(self, temp, humidity, pressure):
        """Updates the displays measurements and dispalys them"""
        self.temperatures.append(self.temperature)
        self.temperature = temp
        self.humidities.append(self.humidity)
        self.humidity = humidity
        self.pressures.append(self.pressure)
        self.pressure = pressure
        self.display()

    def display(self):
        """Displays the average, min, and max measurements"""
        print("Statistics")
        print(f"Average Temp: {sum(self.temperatures)/len(self.temperatures)}")
        print(f"Max Temp: {max(self.temperatures)}")
        print(f"Min Temp: {min(self.temperatures)}")
        print(f"Average Humidity: {sum(self.humidities)/len(self.humidities)}")
        print(f"Max Humidity: {max(self.humidities)}")
        print(f"Min Humidity: {min(self.humidities)}")
        print(f"Average Pressure: {sum(self.pressures)/len(self.pressures)}")
        print(f"Max Pressure: {max(self.pressures)}")
        print(f"Min Pressure: {min(self.pressures)}")
        print("========================")

class ForecastDisplay(Observer):
    """Class representation of a forcast display"""
    def __init__(self, weather_data):
        """Creates a new ForcastDispaly object"""
        self.temperature = 0
        self.humidity = 0
        self.pressure = 0

        self.weather_data = weather_data
        weather_data.register_observer(self)

    def display(self):
        """Dispalys the forcasts temp, humidity, and pressure"""
        print("Forcast")
        print(f"Temperature: {self.temperature + 0.11 * self.humidity + 0.2 * self.pressure}")
        print(f"Humidity: {self.humidity - 0.9 * self.humidity}")
        print(f"Pressure: {self.pressure + 0.1 * self.temperature - 0.21 * self.pressure}")
        print("========================")

class WeatherStation:
    """Class representation of the weather station"""
    def main(self):
        """Creates a new WeatherStation object"""
        weather_data = WeatherData()
        current_display = CurrentConditionsDisplay(weather_data)
        statistics_display = StatisticsDisplay(weather_data)
        forecast_display = ForecastDisplay(weather_data)

        # Create two objects from StatisticsDisplay class and
        # ForecastDisplay class. Also, register them to the concrete instance
        # of the Subject class so they get the measurements' updates.

        # The StatisticsDisplay class should keep track of the min/average/max
        # measurements and display them.

        # The ForecastDisplay class shows the weather forecast based on the current
        # temperature, humidity and pressure. Use the following formulas :
        # forcast_temp = temperature + 0.11 * humidity + 0.2 * pressure
        # forcast_humadity = humidity - 0.9 * humidity
        # forcast_pressure = pressure + 0.1 * temperature - 0.21 * pressure

        weather_data.set_measurements(80, 65,30.4)
        weather_data.set_measurements(82, 70,29.2)
        weather_data.set_measurements(78, 90,29.2)

        # un-register the observers
        weather_data.remove_observer(current_display)
        weather_data.remove_observer(statistics_display)
        weather_data.remove_observer(forecast_display)
        weather_data.set_measurements(120, 100,1000)


if __name__ == "__main__":
    w = WeatherStation()
    w.main()
