#HIERARCHICAL INHERITANCE:
#           if multiple derived class is inherited from one base class
#                            dad=====> son1+son2+son3


#base class
class dad():
    def money(self):
        print("dads money")


#derived class
class son1(dad):
    pass


#derived class
class son2(dad):
    pass


#derived class
class son3(dad):
    pass

s2=son2()
s2.money()
