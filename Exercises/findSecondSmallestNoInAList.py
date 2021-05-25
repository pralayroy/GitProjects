def second_smallest(number):
    l = len(number)
    if l < 2:
        return
    if (l == 2) and (number[0] == number[1]):
        return
    dup_items = set()
    uniq_items = []
    for x in number:
        if x not in dup_items:
            uniq_items.append(x)
            dup_items.add(x)
    uniq_items.sort()
    return uniq_items[1]


print(second_smallest([3, 4, 9, 0, 6]))
