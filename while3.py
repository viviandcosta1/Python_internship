table = int(input("enter the number:"))

iteration = int(input("enter the number:"))
total_sum = 0
i = 1

while i<=iteration:
    result = table*i
    print(result)
    total_sum += result
    i += 1
print(total_sum)