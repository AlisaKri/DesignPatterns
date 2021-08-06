from abc import ABC, abstractmethod

# define abstract class FlyBehavior
# difference with the Java implementation that this is an abstract class
# and not an Interface. Since interface is basically an abstract class with
# only methods, this works.

class FlyBehavior(ABC):
    @abstractmethod
    def fly(self):
        pass


# define subclasses for flying:

class FlyWithWings(FlyBehavior):
    def fly(self):
        print("I am flying")

class FlyNoWay(FlyBehavior):
    def fly(self):
        print("I cannot fly")

class FlyRocketPowered(FlyBehavior):
    def fly(self):
        print("I fly Rocket Powered!")
# define abstract class QuackBehavior

class QuackBehavior(ABC):
    @abstractmethod
    def quack(self):
        pass

# define subclasses for quacking behavior

class Quack(QuackBehavior):
    def quack(self):
        print("Quack!")

class MutedQuack(QuackBehavior):
    def quack(self):
        print("<<  Silence >>")

class Squeak(QuackBehavior):
    def quack(self):
        print("Squeak!")

# define a duck parent class
# Difference with Java implementation: Duck is a "normal" class and not
# an abstract class. There is no reasion to make it ABC, because then
# all methods would have to be overriden, according to the abc package implementation

class Duck():
    def __init__(self):
        self.flyBehavior = None
        self.quackBehavior = None
        self.value = "I am a duck"
    
    def display():
        pass
    
    
    def setFlyBehavior(self, fb):
        self.flyBehavior = fb
    def performFly(self):
        self.flyBehavior.fly()

    def performQuack(self):
        self.quackBehavior.quack()

    def swim(self):
        print("All ducks can swim")

class MallardDuck(Duck):
    def __init__(self):
        super().__init__()
        self.flyBehavior = FlyWithWings()
        self.quackBehavior = Quack()

    def display(self):
        print("I am a Mallard Duck!")

class ModelDuck(Duck):
    def __init__(self):
        super().__init__()
        self.flyBehavior = FlyNoWay()
        self.quackBehavior = Quack()

    def display(self):
        print("I am a Model Duck!")

def main():
    mallard = MallardDuck()
    mallard.display()
    mallard.performQuack()
    mallard.performFly()
    mallard.swim()

    model = ModelDuck()
    model.display()
    model.performQuack()
    model.performFly()
    newFlyBehavior = FlyRocketPowered()
    model.setFlyBehavior(newFlyBehavior)
    model.performFly()



if __name__ == "__main__":
    main()




