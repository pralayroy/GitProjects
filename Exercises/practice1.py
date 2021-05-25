list = [1,3,4,5,6,8]
list.append(9)
print(list)
for i in range(1,4):
    list.append(i)
print(list)
list.insert(0, 5)
print(list)
list.extend([11,12,13])
print(list)

list.remove(5)
print(list)
for i in range(1, 3):
    list.remove(i)
print(list)
list.pop(7)
print(list)
list.reverse()
print(list)
list.sort()
print(list)
sliced_list = list[5:]
print(sliced_list)
sliced_list1 = list[:3]
print(sliced_list1)
sliced_list2 = list[1:3]
print(sliced_list2)
sliced_list3 = list[:-2]
print(sliced_list3)
sliced_list4 = list[-2:]
print(sliced_list4)