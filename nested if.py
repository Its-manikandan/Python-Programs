age=int(input("Enter the age:"))
salary=int(input("Enter the salary:"))
if age<=25 or salary>=20000:
    loan=int(input("LOAN:"))
    if loan<=50000:
        print("You are Eligible for Loan")
    else:
        print("Maximum loan amount is 50000")
    print("you are eligible")
else:
    print("You are not Eligible")
