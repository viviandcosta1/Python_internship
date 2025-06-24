num = int(input("enter a number: "))
if num > 0 and num %2 == 0 :
    print("number is positive and even: ") 
elif num > 0 and num %2 != 0:
    print("number is positive and odd: ")
elif num < 0 and num %2 != 0:
    print("number is negetive and odd: ") 
elif num < 0 and num %2 == 0:    
    print("number is even and negative: ")  
else:
    print("number is zero: ")  



