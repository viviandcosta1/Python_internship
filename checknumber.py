def check_number(num):
    if num > 0:
        if num % 2 ==0:
            print(f"{num}the number is even:")
        else:
            print(f"{num}the number is odd:")
    elif num < 0:
        print(f"{num}number is positive:")
    else:
        print("number is zero:")

check_number(1)
check_number(10)
check_number(-7)                      
check_number(0)