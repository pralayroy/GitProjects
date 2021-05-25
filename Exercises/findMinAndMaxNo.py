def getMinMMax(data):
    min_num = data[0]
    max_num = data[0]
    for num in data:
        if num > 1:
            max_num = num
        elif num < 1:
            min_num = num
    return min_num, max_num


data = [-1, 2, 3, 10]
min_num, max_num = getMinMMax(data)
print("Min no is: ", min_num)
print("Max no is: ", max_num)

#print(getMinMMax([1, 2, 3, 4]))
