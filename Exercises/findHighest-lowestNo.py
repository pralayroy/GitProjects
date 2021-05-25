def high_and_low(numbers):
    li = [int(x) for x in numbers.split(' ')]
    print(li)
    mx = max(li)
    mn = min(li)
    return str(mx)+" "+str(mn)


numbers = "1 -2 3 4 5"
print(high_and_low(numbers))
