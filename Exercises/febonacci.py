def febonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return febonacci(n - 1) + febonacci(n - 2)


print(febonacci(10))

