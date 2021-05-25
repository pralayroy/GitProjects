#li = [7, 2, 8, 9, 1, 3, 4]
# Pull out the elements a and b, for which the sum a+b is also in the list
# output here:
# 7,2 -> 9
# 8,1 -> 9
# 1,3 -> 4

list = [7, 2, 8, 9, 1, 3, 4]
size = len(list)
sum = 0
for i in range(size):
    k = i
    for j in range(k, size):
        if list[i] + list[j] == sum[i]:
            print("no present in the list")
        else:
            print("not present in the list")


