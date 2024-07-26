# HYBIRD INHERIANCE:
#         single + multiple + multilevel + hierarchical====> Hybird

class dad():
    def money(self):
        print("dads money")

class land():
    def property(self):
        print("My Land")
        
class son1(dad,land):
    pass

class son2(dad):
    pass

class son3(dad):
    pass

s2=land()
s2.property()
