from abc import ABC, abstractmethod

# interfaces

class Subject(ABC):
    @abstractmethod
    def registerObserver(self, observer):
        pass
    @abstractmethod
    def removeObserver(self, observer):
        pass
    @abstractmethod
    def notifyObservers(self):
        pass

class Observer(ABC):
    @abstractmethod
    def update(self):
        pass

class DisplayElement(ABC):
    @abstractmethod
    def display(self):
        pass

# concrete observer class

class WeatherData(Subject):
    def __init__(self):
        super().__init__()
        self.observersList = []
        self.temperature = None
        self.pressure = None
        self.humidity = None
        

    def registerObserver(self, observer):
        if observer not in self.observersList:
            self.observersList.append(observer)

    def removeObserver(self, observer):
        if observer in self.observersList:
            self.observersList.remove(observer)

    def notifyObservers(self):
        for observer in self.observersList:
            observer.update(self.temperature, self.humidity, self.pressure)

    # this observer specific methods
    def setConditions(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure 
        self.measurementsChanged()

    def measurementsChanged(self):
        self.notifyObservers()

# concrete displayElement:

class CurrentConditionsDisplay(Observer, DisplayElement):
    def __init__(self, weatherData):
        super().__init__()
        self.temperature = None
        self.humidity = None
        self.weatherData = weatherData
        # the key part: register to the observer!
        self.weatherData.registerObserver(self)

    def update(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.display()

    def display(self):
        print("Current Conditions: ", self.temperature, "F degrees and ", self.humidity, "% humidity")


def main():
    # instantiate the subject
    weatherData = WeatherData()
    # instantiate the display
    currentConditionsDisplay = CurrentConditionsDisplay(weatherData)
    #subscribe 
    # set measurements
    weatherData.setConditions(80, 73, 540)
    weatherData.setConditions(-100,33,15)


if __name__ == "__main__":
    main()










