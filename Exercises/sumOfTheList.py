def search(a, b):
    for d in b:
        if a == d:
            m = True
            break
        else:
            m = False
    return m


x = [1, 4, 5, 7, 9, 6, 2]
target = int(input("Enter the number:"))
for i in x:
    if i < target:
        pair = int(target) - int(i)
        num = search(pair, x)
        if pair in x:
            print("the first number= %d the second number %d" % (i, pair))
            break
