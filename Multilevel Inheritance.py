#MULTILEVEL INHERITANCE:
#            it involves inheriting a class that has already inherited with some other class.
#                              base class 1 + base class 2 ====> derived class 



#base class

class grandpa():
    def car(self):
        print("grandpa car")

#base class
        
class dad(grandpa):
    def bike(self):
        print("dad bike")

#derived class
        
class son(dad):
    def cycle(self):
        print("sons cycle")

ram=son()
ram.cycle()
ram.bike()
ram.car()

GK=dad()
GK.car()

GD=grandpa()
GD.car()
