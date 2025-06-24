def pascal_traingle(rows):
    traingle = []
    row_num = 0
    while row_num < rows:
        row = []
        item_num = 0
        while item_num <= row_num:
            if item_num == 0 or item_num == row_num:
                row.append(1)
            else:
                row.append(traingle[row_num -1][item_num -1]+ traingle[row_num-1][item_num]) 
            item_num += 1
        traingle.append(row)
        row_num += 1

        max_width = len(''.join(map(str,traingle[-1])))
        for row in traingle:
            print(''.join(map(str,row)).center(max_width))

pascal_traingle(5)                     