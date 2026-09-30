from abc import ABC, abstractmethod

class Animal(ABC):
    def move(self):
        pass


class Human(Animal):
        def move(self):
            print("I can walk")



class Cat(Animal):
        def move(self):
            print("i can jump from whatever height")




class Dog(Animal):
        def move(self):
            print("I can bark")


class Bird(Animal):
        def move(self):
            print("I can fly")


class Snake(Animal):
        def move(self):
              print("I can crawl")


H = Human()
H. move()


C = Cat()
C. move()

D = Dog()
D. move()

B = Bird()
B.move()


S = Snake()
S.move()
