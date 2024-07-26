a="EMC"
b=123

c=str(input("Enter the username:"))
d=int(input("Enter the password:"))

def validate():
    if a==c and b==d:
        return True
    else:
        return False

z=validate()
print(z)
