score=int(input("Enter the score:"))
if score<35:
    print("poor Student")
elif score>35 and score<70:
    print("Average student")
elif score>70 and score<100:
    print("Brilliant Student")
else:
    print("Invalid number")
