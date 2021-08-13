from abc import ABC, abstractmethod

# Implementation details:
# Cost and Description are set to class attributes, get description for beverage are class methods
# Reason: Instantiating an object = order, asking for price and description of class is reading the menu.

# Beverage also has class methods: getDescription, myCost and setCost.

# The object method getCost is for calculating the cost of an actual drink.

# Condiment Decorator inherits from Beverage, so upon wrapping, the type of the variable doesn't change. 
# For example, beverage = HouseBlend (black coffee) and beverage = Milk(HouseBlend()) (coffee with milk) 
# are still an instance of beverage

# Condiment Decorator overrides Beverage's description classmethod, to make it additive
# The getCost of is an abstract method to allow for different implementations. For instance, Milk and Sugar are free.

# The benefit of cost being a class attribute and not an object attribute is being able to change prices of specific ingredients dynamically,
# such as setting a certain type of roast on a discount or increasing the prize of whipped cream because of a national shortage


class Beverage(ABC):
    # class variables
    cost = None
    description = "Unknown Beverage"

    # class methods
    @classmethod
    def getDescription(cls):
        return cls.description
    
    @classmethod
    def myCost(cls):
        return cls.cost
        
  
    @classmethod
    def setCost(cls, cost):
        cls.cost = cost

    @classmethod
    def setDiscount(cls,discount):
        cost = cls.cost * discount
        cls.setCost(cost)

    # object methods
    def getCost(self):
        return self.cost
    
# actual beverages

class HouseBlend(Beverage):

    cost = 2.99
    description = "House Blend"
        



class DeCaf(Beverage):
    cost = 2.99
    description = "Decaf"


class Espresso(Beverage):

    cost = 1.99
    description = "Espresso"



# Condiment decorator

class CondimentDecorator(Beverage, ABC):

    cost = None
    descritpion = "Unkonwn condiment"
    def __init__(self):
        self.beverage = None



    def getDescription(self):
        return self.beverage.getDescription() + ", " + self.description

    #def getCost(self):
    #    return self.beverage.getCost() + self.cost
    @abstractmethod
    def getCost(self):
        pass



# actual decorators

class Milk(CondimentDecorator):
  
    cost = 0
    description = 'Milk'
    def __init__(self, beverage, ):
        self.beverage = beverage

    def getCost(self):
        return self.beverage.getCost() 

   

class Mocha(CondimentDecorator):

    cost = 0.50
    description = 'Mocha'
    def __init__(self, beverage):
        self.beverage = beverage


    def getCost(self):
        return self.beverage.getCost() + self.cost

class CoconutMilk(CondimentDecorator):
    cost = 0.70
    description = 'Coconut Milk'
    
    def __init__(self, beverage):
        self.beverage = beverage  


    def getCost(self):
        return self.beverage.getCost() + self.cost

class Whip(CondimentDecorator):

    cost = 0.80
    description = 'Whip'
    def __init__(self, beverage):
        self.beverage = beverage

    def getCost(self):
        return self.beverage.getCost() + self.cost

class Sugar(CondimentDecorator):

    cost = 0
    description = 'Sugar'
    def __init__(self, beverage):
            self.beverage = beverage
            
    def getCost(self):
        return self.beverage.getCost() 

def main():
    print('\n')

    print('Client: What is your featured drink of the day?')
    print(f'Barista: {HouseBlend.getDescription()}')
    print('Client: How much does it cost?')
    print(f'Barista: {HouseBlend.myCost():.2f}')
    print('Client: Give me one with coconut milk and sugar, please')
    print(f'Barisa: Coconut milk is {CoconutMilk.myCost():.2f} extra.')
    print('Client 1: That\'s fine.')
    beverage1 = HouseBlend()
    beverage1 = CoconutMilk(beverage1)
    beverage1 = Sugar(beverage1)
    print(f'Barista:  {beverage1.getDescription()}: $ {beverage1.getCost():.2f}')

    print('\n')
    print('Client 2: Can I have a mocha espresso with milk, no sugar?')
    beverage2 = Espresso()
    beverage2 = Mocha(beverage2)
    beverage2 = Milk(beverage2)
    print(f'Barista:  {beverage2.getDescription()}: $ {beverage2.getCost():.2f}')

    print('\n')

    print('Push notification from corporate: House Blend is 20% off today!')
    HouseBlend.setDiscount(0.80)
    print('\n')

    print('Client 1: Wait, what do I owe you then?')
    print(f'Barista:  {beverage1.getDescription()}: $ {beverage1.getCost():.2f}')
    print('Client 1: ....')
    print('Barista: Coconut milk is still full price')
    print('Client 1: Oh.')

    print('\n')
    print('There is a national shortage of whipped cream! Temporary price increase to 90 cents')
    print(f'Old menu: Whipped cream = {Whip.myCost():.2f}')
    Whip.setCost(0.90)
    print(f'New menu: Whipped cream = {Whip.myCost():.2f}')

if __name__ == "__main__":
    main()


