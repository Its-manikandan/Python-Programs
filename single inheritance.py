#SINGLE INHERITANCE
              #single derived class is inherited from single Base class
                     #BASE CLASS <---------- DERIVED CLASS

#Base class
class dad():
    def money(self):
        print("dads money")

        
#Derived class
class son(dad):
    def phone(self):
        print("sons phone")

ram=son()
ram.phone()
ram.money()
        
