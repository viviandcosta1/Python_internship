table = int(input("enter the number:"))
iteration = int(input("enter the number:"))

i = 1
total_sum = 0

while i <= iteration:
    result = table*i
    print(result)

    j = 1
    temp_sum = 0
    while j <= i:
        temp_sum +=(table*j)
        j +=1
    total_sum = temp_sum
    i += 1
print(total_sum)