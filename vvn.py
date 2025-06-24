rows=int(input("enter the rows:"))
i = 1
while i <= rows:
    space = "  " * (rows-i)
    ones = (str(i)+" ") * i 
    print(space + ones)
    i += 1


    j = 2
    while j<=rows:
        total = "  " * (rows-j)
        two = (str(j)+" ")* j 
        print(total + two)
        j += 1