from abc import ABC, abstractmethod

# define abstract class FlyBehavior

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

class Duck():
    def __init__(self):
        self.flyBehavior = None
        self.quackBehavior = None
        self.value = "I am a duck"
    
    def display():
        pass
    
    # Important: pass the function into the setter and assing the function call within the setter
    def setFlyBehavior(self, fb):
        self.flyBehavior = fb()
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
    model.setFlyBehavior(FlyRocketPowered)
    model.performFly()



if __name__ == "__main__":
    main()




