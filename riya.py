rows=int(input("enter the rows:"))
j = 0
num = 1
while j <= i:
    print(num, end= "   ")
    num = num * (i - j) // (j+1)
    j += 1

    print()
    i += 1 

    i = 0

    while i <= rows:
        space = 1
        while space < rows - i - 1:
            print(" ", end=" ")
            space += 1   
