class goa():
    name=""
    drink=""
    def party(self):
        print("Lets party.....")
    def beach(self):
        print("Beach porom")

Firstperson=goa()
Secondperson=goa()

Firstperson.name="ramesh"
Secondperson.name="suresh"

Firstperson.drink="Yes"
Secondperson.drink="No"

print(Firstperson.name)
print("Drink",Firstperson.drink)

Firstperson.party()

print(Secondperson.name)
print("Drink",Secondperson.drink)

Secondperson.beach()

        
