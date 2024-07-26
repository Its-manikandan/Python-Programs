class teacher:
    def __init__(self,name,register):
        self.name=name
        self.register=register 
     def display(self):
        print("NAME:",self.name)
        print("REGISTER:",self.register)
        
T1=teacher("MS.MOHAMED RITHAVUDEEN","3024")
T2=teacher("MANIKANDAN","3017")

T1.display()
T2.display()

