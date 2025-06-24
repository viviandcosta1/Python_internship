age = int(input("enter the age :"))

if age < 13:
    print("you are a child: ")

elif age < 20:
    print("you are a teenager: ")

elif age < 60:
    print("you are a adult: ")

elif age %1 == 0:
    print("you are a senior: ")  

else:
    print("your age is invalid: ")        