list = [1,2,4]
res = [x for x in range(list[0], list[-1]+1) if x not in list]
print(res)