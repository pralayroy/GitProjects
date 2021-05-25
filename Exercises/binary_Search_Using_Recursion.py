# binary search using recursion

def binarySearch(list, start, end, key):
    if not start < end:  # searching the key
        return -1

    midd = (start + end) // 2  #start = 0 length of the li
    if list[midd] < key:
        return binarySearch(list, midd+1, end, key) #
    elif list[midd] > key:
        return binarySearch(list, start, midd, key)
    else:
        return midd


list = [3, 5, 10, 20, 15, 50]
#list1 = list.split()
a = 25
finalResult = binarySearch(list, 0, len(list)-1, a)
if finalResult < 0:
    print("Not present")
else:
    print("Ele is present", str(finalResult))





