class laptop:
    chargertype="C TYPE"

    def __init__(self):
        self.brand=""
        self.price="56"

    def setprice(self,price):
        self.price=price

    def getprice(self):
        print(self.price)

#To change the class variable value:
        # we need to mention the (cls)
    @classmethod
    def changechargertype(cls):
        cls.chargertype="B TYPE"
        print("charger was changed")

    @staticmethod
    def info():
        print("Laptop class")

hp=laptop()
hp.setprice(45777)
hp.getprice()

laptop.changechargertype()

hp.info()
            
        
