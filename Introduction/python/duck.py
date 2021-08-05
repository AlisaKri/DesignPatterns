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

def main():
    mallard = MallardDuck()
    mallard.performQuack()
    mallard.performFly()
    mallard.swim()


if __name__ == "__main__":
    main()



