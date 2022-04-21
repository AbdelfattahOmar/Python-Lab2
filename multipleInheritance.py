class Human:
    def eat(self):
        print("Eat from class Human")

class Mammal:
    def eat(self):
        print("Eat from class Mammal")

class Person(Human,Mammal) :
    pass

person = Person()
person.eat()
   

