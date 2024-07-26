#Instance variable:
    #it is used for different values through constructor[__init__(self)]
class phone():
    def __init__(self,brand,price,chargertype):
        self.brand=brand
        self.price=price
        self.chargertype=chargertype
    def display(self):
        print("BRAND:",self.brand)
        print("PRICE:",self.price)
        print("chargertype:",self.chargertype)

samsung=phone("samsung","50000","C-TYPE")
samsung.display()

redmi=phone("redmi","50000","C_TYPE")
redmi.display()     
     

#class variable:
    # it is used for same values, it will be defined in class.
    # Example--> class phone():
     #                 chargertype="C TYPE"

class phone():
    chargertype="C-TYPE"
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
    def display(self):
        print("BRAND:",self.brand)
        print("PRICE:",self.price)
        print("chargertype:",self.chargertype)

samsung=phone("samsung","50000")
samsung.display()

redmi=phone("redmi","50000")
redmi.display()     
     

