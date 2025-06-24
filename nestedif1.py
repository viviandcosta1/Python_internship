num = int(input("enter a number: "))
if num > 0:
    print("number is positive: ")
    if num %2 == 0:
        print("number is even: ")
    else:
        print("number is odd: ")    

elif num < 0:
    print("number is negative: ") 
    if num %2 == 0:
        print("number is even: ") 
    else:
        print("number is odd: ")
else:
    print("its zerozero")