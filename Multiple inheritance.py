#MULTIPLE INHERITANCE:
#           If a derived class inherted from more than one base class
#                      dad & mom
#                         son


#BASE CLASS
class dad():
    def money(self):
        print("Dads money")



#BASE CLASS
class mom():
    def sweet(self):
        print("moms sweet")


#DERIVED CLASS
class son(dad,mom):
    def laptop(self):
        print("sons laptop")

ram=son()
ram.sweet()
ram.money()

        
        
