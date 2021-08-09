# a model with an observable superclass that can manage subscribers with pull or push notifications

from abc import ABC, abstractmethod
from collections import defaultdict


# for push-pull, Subject will be a class with push-pull methods and Subject will inherit from that class

class Observable():

    def __init__(self):
        self.observersDict = defaultdict(list)
        self.changed = False
    
    # these methods are now for those who want to get push notifications for updates
    def registerObserver(self, observer, mode='push'):
        if observer not in self.observersDict:
            self.observersDict[mode].append(observer)
    
    def removeObserver(self, observer):
        if observer in self.observersDict['push']:
            self.observersDict['push'].remove(observer)
        if observer in self.observersDict['pull']:
            self.observersDict['pull'].remove(observer)

    def changeObserverMode(self, observer):
        if observer in self.observersDict['push']: 
            self.observersDict['push'].remove(observer)
            self.observersDict['pull'].append(observer)
        else:
            self.observersDict['pull'].remove(observer)
            self.observersDict['push'].append(observer)
    
    # in java.utils there are two versions of the notifyObservers method, 
    # dependoing on whether observer object is passed
    def notifyObservers(self, data = None):
        if (self.changed):
            for observer in self.observersDict['push']:
                observer.update(self, data)
            for observer in self.observersDict['pull']:
                observer.update(self)
            self.changed = False
        

    # new methods for this new pattern:
    # notifyObservers only sents out notifications of the status changed
    # allows to optimize notifications, to set thresholds to changes etc
    def setChanged(self):
        self.changed = True

    def clearchanged(self):
        self.changed = False

    def hasChanged(self):
        return self.changed





# interfaces
class Observer(ABC):
    @abstractmethod
    def update(self, observable, data):
        pass

class DisplayElement(ABC):
    @abstractmethod
    def display(self):
        pass

# concrete observer class

class WeatherData(Observable):
    
    def __init__(self):
        super().__init__()
        
        self.temperature = None
        self.pressure = None
        self.humidity = None    


    # this observer specific methods
    def setConditions(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure 
        # potentially here set a condition on whether change is significant enough
        # to call setChanged and measurementsChanged
        self.setChanged()
        data = {
            'temperature': temperature,
            'humidity': humidity,
            'pressure': pressure
        }
        self.measurementsChanged(data)

    def measurementsChanged(self, data):
        self.notifyObservers(data)

    # these methods are for those who want to pull their own data

    def getTemperature(self):
        return self.temperature

    def getHumidity(self):
        return self.humidity

    def getPressure(self):
        return self.pressure

# concrete displayElement:

class CurrentConditionsDisplay(Observer, DisplayElement):
    def __init__(self, observable, mode="push"):
        super().__init__()
        self.temperature = None
        self.humidity = None
        self.mode = mode
        # this can be the higher class, so I can have multiple subjects pushing notifications
        self.observable = observable
        self.observable.registerObserver(self, mode)

    
    def changeMode(self, observable):
        self.observable.changeObserverMode(self)
        

    def update(self, observable, data=None):
        # pull mode:
        if data == None:
            print('receiving pull notification')
            if isinstance(observable, WeatherData):
                self.temperature = observable.getTemperature()
                self.humidity = observable.getHumidity()
        # push mode:
        else:
            print('receiving push notification')
            self.temperature = data['temperature']
            self.humidity = data['humidity']
        self.display()

    def display(self):
        print("Current Conditions: ", self.temperature, "F degrees and ", self.humidity, "% humidity")

class humidityIndex(Observer, DisplayElement):

    def __init__(self, weatherData):
        super().__init__()
        self.temperature = None
        self.humidity = None
        self.weatherData = weatherData
        #

def main():
    # instantiate the subject
    weatherData = WeatherData()
    # instantiate the display
    currentConditionsDisplay = CurrentConditionsDisplay(weatherData, 'push')
    #subscribe 
    # set measurements
    weatherData.setConditions(80, 73, 540)
    weatherData.setConditions(-100,33,15)

    currentConditionsDisplay.changeMode(weatherData)
    weatherData.setConditions(90, 63, 440)



if __name__ == "__main__":
    main()










