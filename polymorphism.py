#polymorphism:
#           poly===>more  and   morphism===>change their structure and function
# oru function andhandha activity adopt agura mari thanna maathikichina, it is called polymorphism..


def plus(a,b,c=0):
    print(a+b+c)
plus(1,2)
plus(1,2,3)

#method overrides: it is also polymorphism.
#           it allows you to redefine the method in subclass which is previously defined in the main class.


class animal():
    def sound(self):
        print("Animal makes a sound")

class dog(animal):
    def sound(self):
        print("Dog Barks")

class bird(animal):
    def sound(self):
        print("Birds sing")
    
 
        

jimmy=dog()
jimmy.sound()

jintu=bird()
jintu.sound()
        
