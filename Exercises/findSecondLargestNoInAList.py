list = [0, 20, 30, 5, 10, 2]
mx = max(list[0], list[1])
secondmax = min(list[0], list[1])
n = len(list)
for i in range(2, n):
    if list[i] > mx:
        secondmax = mx
        mx = list[i]
    elif secondmax < list[i] != mx:
        secondmax = list[i]
print("Second highest no is: ", str(secondmax))


