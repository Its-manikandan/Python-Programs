a=int(input("Enter the Tamil Mark:"))
b=int(input("Enter the English Mark:"))
c=int(input("Enter the Maths Mark:"))
d=int(input("Enter the Science Mark:"))
e=int(input("Enter the Social Mark:"))
Add=(a+b+c+d+e)
Average=Add/5

if Average<=35:
    print("You need an Additional class")
else:
    print("keep it up")
    
